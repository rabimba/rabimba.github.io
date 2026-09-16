#!/usr/bin/env python3
"""Sync new publications from OpenAlex + DBLP into content/publication/.

Fetches works for Rabimba Karanjai from both sources, skips anything already
on the site (fuzzy title match), and generates new publication pages using
the site's front-matter template. Run with --dry-run to preview.

Designed for a scheduled GitHub Action: new pages are committed to a branch
and opened as a PR for human review before publishing.
"""

import argparse
import os
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from datetime import date

import requests

OPENALEX_IDS = ["A5016852422", "A5100493788", "A5137309728"]
DBLP_PID = "283/5555"
PUB_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "publication")
MAILTO_UH = "uh.edu"

HEADERS = {"User-Agent": "rabimba-site-pub-sync/1.0 (mailto:contact@rabimba.me)"}

TAG_KEYWORDS = [
    ("LLMs", ["llm", "large language", "gpt", "language model"]),
    ("AI Agents", ["agent"]),
    ("Security", ["secur", "phishing", "ransomware", "vulnerab", "attack"]),
    ("Blockchain", ["blockchain", "smart contract", "defi", "web3", "on-chain", "move", "solidity"]),
    ("Quantum Computing", ["quantum"]),
    ("Code Generation", ["code generation", "code translation", "program repair", "unit test"]),
    ("Privacy", ["privacy", "zero-knowledge", "confidential"]),
    ("Healthcare", ["medical", "diagnos", "health", "microbiota"]),
    ("TPU", ["tpu", "xla", "openxla"]),
]


def norm_title(t):
    s = unicodedata.normalize("NFKD", t or "").lower()
    return re.sub(r"[^a-z0-9]+", "", s)


def make_slug(t):
    s = unicodedata.normalize("NFKD", t).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60].rstrip("-")


def existing_index():
    """Collect normalized titles, DOIs and arXiv IDs from existing pages."""
    titles, dois, arxivs = set(), set(), set()
    if os.path.isdir(PUB_DIR):
        for d in os.listdir(PUB_DIR):
            f = os.path.join(PUB_DIR, d, "index.md")
            if os.path.isfile(f):
                s = open(f, encoding="utf-8").read()
                m = re.search(r"^title:\s*'?(.+?)'?\s*$", s, re.M)
                if m:
                    titles.add(norm_title(m.group(1)))
                for dm in re.findall(r'10\.\d{4,9}/[^\s\'"\n]+', s):
                    dois.add(dm.rstrip('.,)').lower())
                for am in re.findall(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})", s):
                    arxivs.add(am)
                for dm in re.findall(r"10\.48550/arXiv\.([0-9]{4}\.[0-9]{4,5})", s, re.I):
                    arxivs.add(dm)
    return titles, dois, arxivs


def work_arxiv_id(w):
    m = (re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})", w.get("url") or "")
         or re.search(r"10\.48550/arXiv\.([0-9]{4}\.[0-9]{4,5})", (w.get("doi") or "") + " " + (w.get("url") or ""), re.I))
    return m.group(1) if m else None


def is_known(w, titles, dois, arxivs):
    if norm_title(w["title"]) in titles:
        return True
    if w.get("doi") and w["doi"].lower() in dois:
        return True
    ax = work_arxiv_id(w)
    if ax and ax in arxivs:
        return True
    import difflib
    nt = norm_title(w["title"])
    for t in titles:
        if abs(len(nt) - len(t)) <= max(len(nt), len(t)) * 0.25 and difflib.SequenceMatcher(None, nt, t).ratio() >= 0.90:
            return True
    return False


def fetch_openalex():
    works = {}
    for aid in OPENALEX_IDS:
        cursor = "*"
        while cursor:
            r = requests.get(
                "https://api.openalex.org/works",
                params={
                    "filter": f"author.id:{aid}",
                    "per-page": 200,
                    "cursor": cursor,
                    "select": "id,doi,title,display_name,publication_date,publication_year,type,"
                              "authorships,primary_location,abstract_inverted_index",
                },
                headers=HEADERS,
                timeout=60,
            )
            r.raise_for_status()
            data = r.json()
            for w in data.get("results", []):
                works[w["id"]] = w
            cursor = data.get("meta", {}).get("next_cursor")
    out = []
    for w in works.values():
        src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or ""
        authors = [a["author"]["display_name"] for a in w.get("authorships", [])]
        abstract = reconstruct_abstract(w.get("abstract_inverted_index"))
        landing = (w.get("primary_location") or {}).get("landing_page_url") or ""
        out.append({
            "title": w.get("display_name") or w.get("title") or "",
            "date": w.get("publication_date") or f"{w.get('publication_year') or 2000}-01-01",
            "authors": authors,
            "venue": src,
            "wtype": w.get("type") or "article",
            "doi": (w.get("doi") or "").replace("https://doi.org/", ""),
            "abstract": abstract,
            "url": landing if "arxiv.org" in landing else "",
            "source": "OpenAlex",
        })
    return out


def reconstruct_abstract(inv):
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))[:1200]


def fetch_dblp():
    r = requests.get(f"https://dblp.org/pid/{DBLP_PID}.xml", headers=HEADERS, timeout=60)
    r.raise_for_status()
    root = ET.fromstring(r.content)
    out = []
    for rec in root.findall(".//r/*"):
        t = rec.find("title")
        if t is None:
            continue
        title = "".join(t.itertext()).rstrip(".")
        authors = [a.text for a in rec.findall("author") if a.text]
        venue = rec.find("venue")
        booktitle = rec.find("booktitle")
        year = rec.find("year")
        doi = rec.find("doi")
        ee = rec.find("ee")
        ptype = rec.get("type", "")
        out.append({
            "title": title,
            "date": f"{(year.text if year is not None else 2000)}-01-01",
            "authors": authors,
            "venue": (booktitle.text if booktitle is not None else venue.text if venue is not None else ""),
            "wtype": "journal-article" if "Journal" in ptype else ("preprint" if "Informal" in ptype else "conference-paper"),
            "doi": doi.text if doi is not None else "",
            "abstract": "",
            "url": ee.text if ee is not None else "",
            "source": "DBLP",
        })
    return out


def pick(works, key, default=""):
    for w in works:
        if w.get(key):
            return w[key]
    return default


def derive_tags(title, first_author):
    tags = []
    tl = title.lower()
    for tag, kws in TAG_KEYWORDS:
        if any(k in tl for k in kws):
            tags.append(tag)
    if first_author == "Rabimba Karanjai":
        tags.append("First Author")
    return tags or ["Research"]


def pub_type(wtype):
    if wtype in ("preprint", "report", "editorial"):
        return "3"
    if wtype == "journal-article":
        return "2"
    return "1"


def gen_page(w, slug):
    authors = w["authors"] or ["Rabimba Karanjai"]
    first = authors[0] if authors else ""
    ptype = pub_type(w["wtype"])
    venue = w["venue"] or ("arXiv preprint" if ptype == "3" else "Preprint")
    ymd = w["date"][:10]
    links = []
    if w.get("doi"):
        links.append(("DOI", f"https://doi.org/{w['doi']}"))
    if "arxiv.org" in (w.get("url") or ""):
        links.append(("arXiv", w["url"].replace("/abs/", "/pdf/")))
    links_yaml = ""
    if links:
        links_yaml = "links:\n" + "".join(f"- name: {n}\n  url: {u}\n" for n, u in links)
    bibkey = re.sub(r"[^a-z]", "", (authors[0].split()[-1] if authors else "work")).lower() + w["date"][:4]
    bibtype = "article" if ptype == "2" else ("misc" if ptype == "3" else "inproceedings")
    bib = (f"@{bibtype}{{{bibkey},\n  title={{ {w['title']} }},\n"
           f"  author={{ { ' and '.join(authors) } }},\n"
           + (f"  booktitle={{ {venue} }},\n" if bibtype == "inproceedings" else (f"  journal={{ {venue} }},\n" if ptype == '2' else f"  howpublished={{ {venue} }},\n"))
           + f"  year={{ {w['date'][:4]} }}\n}}")
    abstract = (w["abstract"] or "Added automatically from publication feeds — see links for details.").replace('"', "'")
    abstract = re.sub(r"\s+", " ", abstract).strip()
    fm = (
        "---\n"
        f"title: '{w['title'].replace(chr(39), chr(39)*2)}'\n"
        "authors:\n" + "".join(f"- {a}\n" for a in authors) +
        f"date: '{ymd}T00:00:00Z'\n"
        f"doi: '{w.get('doi') or ''}'\n"
        f"publishDate: '{ymd}T00:00:00Z'\n"
        "publication_types:\n"
        f"- '{ptype}'\n"
        f"publication: '{venue.replace(chr(39), chr(39)*2)}'\n"
        f"publication_short: '{venue.replace(chr(39), chr(39)*2)[:40]}'\n"
        f"abstract: '{abstract[:900].replace(chr(39), chr(39)*2)}'\n"
        "tags:\n" + "".join(f"- {t}\n" for t in derive_tags(w['title'], first)) +
        "featured: false\n"
        "draft: false\n" +
        links_yaml +
        'bibtex: "' + bib.replace('"', '\\"').replace("\n", "\\n") + '"\n'
        "---\n\n"
    )
    return fm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    titles, dois, arxivs = existing_index()
    feed = fetch_openalex() + fetch_dblp()

    # dedupe within feed by normalized title; prefer published over preprint, more metadata over less
    def score(w):
        return (w["wtype"] != "preprint", bool(w["abstract"]), bool(w["doi"]), w["source"] == "OpenAlex")
    by_title = {}
    for w in feed:
        k = norm_title(w["title"])
        if not k or len(k) < 15:
            continue
        if k not in by_title or score(w) > score(by_title[k]):
            by_title[k] = w

    new = [w for k, w in by_title.items() if k not in titles and not is_known(w, titles, dois, arxivs)
           and not w["title"].lower().startswith("artifacts for")]
    new.sort(key=lambda w: w["date"], reverse=True)

    print(f"feed works: {len(feed)}, unique: {len(by_title)}, new: {len(new)}")
    used_slugs = set(os.listdir(PUB_DIR)) if os.path.isdir(PUB_DIR) else set()
    for w in new:
        slug = make_slug(w["title"]) or "publication"
        base, i = slug, 2
        while slug in used_slugs:
            slug = f"{base}-{i}"; i += 1
        used_slugs.add(slug)
        print(f"  NEW [{w['source']}] {w['date']} {w['title'][:70]}")
        if not args.dry_run:
            d = os.path.join(PUB_DIR, slug)
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "index.md"), "w", encoding="utf-8") as f:
                f.write(gen_page(w, slug))

    if not new:
        print("No new publications.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
