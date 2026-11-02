#!/usr/bin/env python3
"""Sync blog posts from Blogger Atom feed (rkrants.blogspot.com) into content/blog/.

Fetches recent posts from Blogger, skips posts already present in content/blog/
(while repairing any corrupted CSS/HTML-comment summaries in existing posts),
downloads the lead image as featured.png/jpg, and generates Hugo leaf bundles.
"""

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import xml.etree.ElementTree as ET

import requests

BLOG_FEED_URL = "https://rkrants.blogspot.com/feeds/posts/default?max-results=50"
BLOG_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "blog")
HEADERS = {"User-Agent": "rabimba-site-blog-sync/1.0 (mailto:contact@rabimba.me)"}
INSECURE = False

CORRUPT_SUMMARY_PATTERNS = [
    r"position:\s*absolute",
    r"font-family:\s*monospace",
    r"background:\s*#",
    r"linear-gradien",
    r"paste between BEGIN END",
    r"Paste everything between the BEGIN END",
    r"A wrapper to apply our enhancements",
    r"Replace #REPO_URL",
    r"-->",
    r"^=\s*\"",
    r"^body h1,\s*h2",
]


def http_get(url, **kwargs):
    kwargs.setdefault("headers", HEADERS)
    kwargs.setdefault("timeout", 45)
    if INSECURE:
        kwargs["verify"] = False
    return requests.get(url, **kwargs)


def norm_title(t):
    s = unicodedata.normalize("NFKD", t or "").lower()
    return re.sub(r"[^a-z0-9]+", "", s)


def make_slug(title, alt_url=""):
    if alt_url:
        m = re.search(r"/\d{4}/\d{2}/([a-z0-9-]+)\.html", alt_url.lower())
        if m:
            return m.group(1)[:60].rstrip("-")
    s = unicodedata.normalize("NFKD", title).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60].rstrip("-")


def extract_first_image(html_content):
    if not html_content:
        return ""
    m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', html_content, re.I)
    return m.group(1).strip() if m else ""


def extract_summary(html_content, title=""):
    if not html_content:
        return ""
    # Strip comments, style, script, pre, code, and svg blocks first
    cleaned = re.sub(r"<!--.*?-->", " ", html_content, flags=re.S)
    cleaned = re.sub(r"<(style|script|svg|pre)[^>]*>.*?</\1>", " ", cleaned, flags=re.S | re.I)
    # Prefer paragraphs if available
    paras = re.findall(r"<p[^>]*>(.*?)</p>", cleaned, flags=re.S | re.I)
    candidates = []
    for p in paras:
        txt = html.unescape(re.sub(r"<[^>]+>", " ", p))
        txt = " ".join(txt.split()).strip()
        # Skip bylines or tiny meta lines
        if len(txt) >= 60 and not txt.lower().startswith(("by rabimba", "live studio:", "published ")):
            candidates.append(txt)
    if candidates:
        summary = candidates[0]
    else:
        txt = html.unescape(re.sub(r"<[^>]+>", " ", cleaned))
        txt = " ".join(txt.split()).strip()
        if title and txt.lower().startswith(title.lower()):
            txt = txt[len(title):].strip(" :-•·")
        summary = txt
    if len(summary) > 240:
        summary = summary[:237].rsplit(" ", 1)[0] + "..."
    return summary


def is_corrupt_summary(s):
    if not s or len(s.strip()) < 35:
        return True
    return any(re.search(pat, s, re.I) for pat in CORRUPT_SUMMARY_PATTERNS)


def fetch_blogger_feed():
    r = http_get(BLOG_FEED_URL)
    r.raise_for_status()
    root = ET.fromstring(r.content)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    posts = []
    for entry in root.findall("atom:entry", ns):
        title_el = entry.find("atom:title", ns)
        pub_el = entry.find("atom:published", ns)
        content_el = entry.find("atom:content", ns)
        title = " ".join((title_el.text if title_el is not None and title_el.text else "").split())
        if not title:
            continue
        published = (pub_el.text if pub_el is not None and pub_el.text else "2026-01-01")[:10]
        raw_html = content_el.text if content_el is not None and content_el.text else ""
        alt_url = ""
        for link in entry.findall("atom:link", ns):
            if link.attrib.get("rel") == "alternate":
                alt_url = link.attrib.get("href", "")
                break
        tags = [
            c.attrib.get("term").strip()
            for c in entry.findall("atom:category", ns)
            if c.attrib.get("term")
        ]
        posts.append({
            "title": title,
            "date": published,
            "url": alt_url,
            "tags": tags or ["Blog"],
            "summary": extract_summary(raw_html, title),
            "image_url": extract_first_image(raw_html),
        })
    return posts


def existing_blog_index():
    by_url = {}
    by_norm_title = {}
    if not os.path.isdir(BLOG_DIR):
        return by_url, by_norm_title
    for d in os.listdir(BLOG_DIR):
        f = os.path.join(BLOG_DIR, d, "index.md")
        if not os.path.isfile(f):
            continue
        txt = open(f, encoding="utf-8").read()
        tm = re.search(r"^title:\s*['\"]?(.+?)['\"]?\s*$", txt, re.M)
        if tm:
            by_norm_title[norm_title(tm.group(1))] = f
        for um in re.findall(r"https?://(?:rkrants\.blogspot\.com|blog\.rabimba\.com)/[^\s'\"]+", txt):
            path_part = re.sub(r"^https?://[^/]+", "", um.rstrip("/"))
            by_url[path_part] = f
    return by_url, by_norm_title


def save_featured_image(image_url, dest_dir):
    if not image_url:
        return None
    try:
        r = http_get(image_url, timeout=30)
        if r.status_code != 200 or not r.content:
            return None
        lower_url = image_url.lower().split("?")[0]
        ext = ".jpg" if lower_url.endswith((".jpg", ".jpeg")) else ".png"
        if lower_url.endswith(".gif"):
            # Convert GIF first frame to PNG on macOS (sips) or ImageMagick (convert) for Hugo compatibility
            with tempfile.NamedTemporaryFile(suffix=".gif", delete=False) as tmp:
                tmp.write(r.content)
                tmp_path = tmp.name
            out_png = os.path.join(dest_dir, "featured.png")
            try:
                if shutil.which("sips"):
                    subprocess.run(["sips", "-s", "format", "png", tmp_path, "--out", out_png],
                                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    os.unlink(tmp_path)
                    return out_png
                elif shutil.which("convert"):
                    subprocess.run(["convert", f"{tmp_path}[0]", out_png],
                                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    os.unlink(tmp_path)
                    return out_png
            except Exception:
                pass
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
        dest_path = os.path.join(dest_dir, f"featured{ext}")
        with open(dest_path, "wb") as f:
            f.write(r.content)
        return dest_path
    except Exception as e:
        print(f"  Image download notice ({image_url}): {e}")
        return None


def gen_blog_page(post):
    title_escaped = post["title"].replace("'", "''")
    summary_escaped = (post.get("summary") or "").replace("'", "''")
    tags = post.get("tags") or ["Blog"]
    tags_yaml = "".join(f"- {t}\n" for t in tags)
    summary_line = f"summary: '{summary_escaped}'\n" if summary_escaped else ""
    return (
        "---\n"
        f"title: '{title_escaped}'\n"
        f"date: '{post['date']}T00:00:00Z'\n"
        f"publishDate: '{post['date']}T00:00:00Z'\n"
        "authors:\n"
        "- admin\n"
        f"{summary_line}"
        "tags:\n"
        f"{tags_yaml}"
        "links:\n"
        "  - type: site\n"
        f"    url: {post['url']}\n"
        "type: blog\n"
        "---\n\n"
        f"{post.get('summary') or ''}\n\n"
        f"[Read full post →]({post['url']})\n"
    )


def match_existing_file(post, by_url, by_norm_title):
    path_part = re.sub(r"^https?://[^/]+", "", (post.get("url") or "").rstrip("/"))
    if path_part and path_part in by_url:
        return by_url[path_part]
    nt = norm_title(post["title"])
    if nt in by_norm_title:
        return by_norm_title[nt]
    for k, f in by_norm_title.items():
        if len(nt) >= 20 and len(k) >= 20 and (nt[:25] in k or k[:25] in nt):
            return f
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--insecure", action="store_true")
    args = ap.parse_args()

    if args.insecure:
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        global INSECURE
        INSECURE = True
        print("WARNING: TLS verification disabled (--insecure). Never use in CI.")

    posts = fetch_blogger_feed()
    by_url, by_norm_title = existing_blog_index()
    used_slugs = set(os.listdir(BLOG_DIR)) if os.path.isdir(BLOG_DIR) else set()

    new_count = 0
    repaired_count = 0

    for p in posts:
        existing_file = match_existing_file(p, by_url, by_norm_title)
        if existing_file:
            # Check if existing file has a corrupt summary we can repair
            txt = open(existing_file, encoding="utf-8").read()
            sm = re.search(r"^summary:\s*([^\n]+(?:\n  [^\n]+)*)", txt, re.M)
            cur_sum = sm.group(1).strip().strip("'\"") if sm else ""
            if sm and is_corrupt_summary(cur_sum) and p.get("summary") and not is_corrupt_summary(p["summary"]):
                clean_sum = p["summary"].replace("'", "''")
                updated = re.sub(r"^summary:\s*[^\n]+(?:\n  [^\n]+)*", f"summary: '{clean_sum}'", txt, count=1, flags=re.M)
                if updated != txt:
                    repaired_count += 1
                    slug_name = os.path.basename(os.path.dirname(existing_file))
                    print(f"  REPAIR-SUMMARY [{slug_name}]")
                    if not args.dry_run:
                        with open(existing_file, "w", encoding="utf-8") as out_f:
                            out_f.write(updated)
            continue

        slug = make_slug(p["title"], p.get("url") or "")
        base, i = slug, 2
        while slug in used_slugs:
            slug = f"{base}-{i}"
            i += 1
        used_slugs.add(slug)
        new_count += 1
        print(f"  NEW BLOG [{p['date']}] {p['title']} -> content/blog/{slug}/")
        if not args.dry_run:
            dest_dir = os.path.join(BLOG_DIR, slug)
            os.makedirs(dest_dir, exist_ok=True)
            with open(os.path.join(dest_dir, "index.md"), "w", encoding="utf-8") as out_f:
                out_f.write(gen_blog_page(p))
            save_featured_image(p.get("image_url"), dest_dir)

    print(f"Blogger feed posts: {len(posts)}, repaired summaries: {repaired_count}, new posts: {new_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
