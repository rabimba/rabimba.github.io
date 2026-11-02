#!/usr/bin/env python3
"""Audit GitHub repositories for rabimba against content/_index.md and content/projects/.

Outputs a summary of any recent non-fork GitHub repositories not yet featured
on the website so the weekly automation PR can surface them for review.
"""

import argparse
import glob
import os
import re
import sys

import requests

GITHUB_USER = "rabimba"
ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
HEADERS = {"User-Agent": "rabimba-site-github-sync/1.0 (mailto:contact@rabimba.me)"}
INSECURE = False

IGNORE_REPOS = {
    "rabimba.github.io",
    "rabimba",
    "baypujo",
    "houstonpujo",
    "getfit",
}


def http_get(url, **kwargs):
    kwargs.setdefault("headers", HEADERS)
    kwargs.setdefault("timeout", 30)
    if INSECURE:
        kwargs["verify"] = False
    return requests.get(url, **kwargs)


def existing_github_repos():
    """Return lowercase repo names already referenced in content/_index.md or content/projects/."""
    found = set()
    paths = [os.path.join(ROOT_DIR, "content", "_index.md")] + glob.glob(
        os.path.join(ROOT_DIR, "content", "projects", "*", "index.md")
    )
    for p in paths:
        if not os.path.isfile(p):
            continue
        txt = open(p, encoding="utf-8").read()
        for m in re.findall(r"github\.com/rabimba/([A-Za-z0-9_.-]+)", txt):
            found.add(m.lower().rstrip("/"))
    return found


def fetch_github_repos(min_year=2026):
    url = f"https://api.github.com/users/{GITHUB_USER}/repos?sort=updated&per_page=50"
    r = http_get(url)
    r.raise_for_status()
    out = []
    for repo in r.json():
        if repo.get("fork") or repo.get("archived"):
            continue
        name = repo.get("name") or ""
        if name.lower() in {x.lower() for x in IGNORE_REPOS}:
            continue
        updated = (repo.get("updated_at") or "")[:10]
        pushed = (repo.get("pushed_at") or "")[:10]
        if pushed and int(pushed[:4]) < min_year:
            continue
        out.append({
            "name": name,
            "html_url": repo.get("html_url") or f"https://github.com/{GITHUB_USER}/{name}",
            "description": repo.get("description") or "",
            "language": repo.get("language") or "",
            "stars": repo.get("stargazers_count") or 0,
            "pushed_at": pushed,
            "updated_at": updated,
            "homepage": repo.get("homepage") or "",
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--insecure", action="store_true")
    ap.add_argument("--report-file", default="")
    args = ap.parse_args()

    if args.insecure:
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        global INSECURE
        INSECURE = True

    known = existing_github_repos()
    repos = fetch_github_repos()
    unlisted = [r for r in repos if r["name"].lower() not in known]

    print(f"GitHub repos checked: {len(repos)}, already on site: {len(known)}, unlisted (2026+): {len(unlisted)}")
    for r in unlisted:
        desc = f" — {r['description']}" if r["description"] else ""
        print(f"  UNLISTED [{r['pushed_at']}] {r['name']} ({r['language'] or 'misc'}, ★{r['stars']}){desc}")

    if args.report_file and unlisted:
        with open(args.report_file, "w", encoding="utf-8") as f:
            f.write("### Recent GitHub Repositories Not Yet on Homepage\n\n")
            for r in unlisted:
                desc = f": {r['description']}" if r["description"] else ""
                f.write(f"- [`{r['name']}`]({r['html_url']}) ({r['language'] or 'Code'}, ★{r['stars']}, pushed {r['pushed_at']}){desc}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
