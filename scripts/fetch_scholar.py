#!/usr/bin/env python3
"""
Fetch publications from Google Scholar and sync to Hugo content/publication/ directory.
Run before 'hugo build' in CI to keep publications up to date.

Usage:
  python scripts/fetch_scholar.py          # full sync
  python scripts/fetch_scholar.py --dry-run  # preview changes without writing
  python scripts/fetch_scholar.py --export-only  # only export data/publications.yaml from existing files
"""
import argparse
import logging
import os
import re
import sys
import time
from pathlib import Path

import yaml

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

SCHOLAR_ID = "PYmmdne2aRMC"
AUTHOR_NAME = "Rabimba Karanjai"
CONTENT_DIR = Path("content/publication")
DATA_DIR = Path("data")

TOPIC_KEYWORDS = {
    "Blockchain": ["blockchain", "smart contract", "ethereum", "solidity", "dapp", "decentral", "web3", "diac", "faas", "cross-chain"],
    "AI": ["artificial intelligence", "machine learning", "neural network", "deep learning", "transformer", " ai "],
    "LLM": ["large language model", "llm", "gpt", "chatgpt", "hallucination", "prompt", "in-context", "language model"],
    "Security": ["security", "privacy", "authentication", "cryptograph", "ransomware", "vulnerability", "trusted execution", "tee", "enclave"],
    "Quantum": ["quantum", "qubit"],
    "Agents": ["agent", "multi-agent", "agentic", "autonomous agent"],
    "IoT": ["iot", "internet of things", "edge computing"],
    "HPC": ["high performance", "hpc", "parallel computing", "accelerat"],
    "Distributed Systems": ["distributed system", "consensus", "fault toleran", "replication", "decentralized infra"],
    "Software Engineering": ["software engineering", "code generation", "program synthesis", "static analysis", "verification"],
    "Computer Vision": ["virtual reality", "vr", "augmented reality", "3d rendering", "image classification", "vision language"],
    "Health AI": ["health", "medical", "clinical", "diagnosis", "disease", "biomedical", "atherosclerosis", "vascular"],
}

TYPE_MAP = {
    "0": "Uncategorized", "1": "Conference", "2": "Journal",
    "3": "Preprint", "4": "Report", "5": "Book",
    "6": "Book Section", "7": "Thesis", "8": "Patent",
}


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s[:60].rstrip("-")


def auto_tag(title: str, abstract: str = "", venue: str = "") -> list[str]:
    text = f"{title} {abstract} {venue}".lower()
    return [topic for topic, kws in TOPIC_KEYWORDS.items() if any(kw in text for kw in kws)]


def infer_pub_type(venue: str) -> str:
    v = venue.lower()
    if any(x in v for x in ["patent", "us patent"]):
        return "8"
    if any(x in v for x in ["thesis", "dissertation"]):
        return "7"
    if any(x in v for x in ["arxiv", "preprint", "under review", "biorxiv"]):
        return "3"
    if any(x in v for x in ["transaction", "journal", "magazine", "tnsm", "tifs", "tkde"]):
        return "2"
    return "1"


def parse_frontmatter(filepath: Path) -> tuple[dict, str]:
    text = filepath.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
        return fm, parts[2]
    except yaml.YAMLError:
        return {}, text


def write_pub_file(slug: str, fm: dict, body: str = "", dry_run: bool = False) -> Path:
    folder = CONTENT_DIR / slug
    filepath = folder / "index.md"
    yaml_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False)
    content = f"---\n{yaml_str}---\n{body}"
    if not dry_run:
        folder.mkdir(parents=True, exist_ok=True)
        filepath.write_text(content, encoding="utf-8")
    return filepath


def load_existing() -> dict[str, dict]:
    """Return dict keyed by normalised title."""
    existing = {}
    if not CONTENT_DIR.exists():
        return existing
    for pub_dir in CONTENT_DIR.iterdir():
        if not pub_dir.is_dir():
            continue
        index = pub_dir / "index.md"
        if not index.exists():
            continue
        fm, body = parse_frontmatter(index)
        if fm.get("title"):
            key = fm["title"].lower().strip()
            existing[key] = {"slug": pub_dir.name, "fm": fm, "body": body}
    return existing


def fetch_scholar_publications() -> list[dict] | None:
    try:
        from scholarly import scholarly
    except ImportError:
        log.error("scholarly not installed — run: pip install scholarly")
        return None

    log.info(f"Fetching publications for Scholar ID: {SCHOLAR_ID}")
    try:
        author = scholarly.search_author_id(SCHOLAR_ID)
        author = scholarly.fill(author, sections=["publications"])
    except Exception as exc:
        log.warning(f"Scholar author fetch failed: {exc}")
        return None

    results = []
    pubs = author.get("publications", [])
    log.info(f"Scholar returned {len(pubs)} publications — filling details...")

    for i, pub in enumerate(pubs):
        try:
            pub = scholarly.fill(pub)
        except Exception as exc:
            log.warning(f"  Could not fill pub {i}: {exc}")

        bib = pub.get("bib", {})
        title = (bib.get("title") or "").strip()
        if not title:
            continue

        raw_authors = bib.get("author", "")
        if isinstance(raw_authors, str):
            authors = [a.strip() for a in re.split(r"\s+and\s+", raw_authors) if a.strip()]
        elif isinstance(raw_authors, list):
            authors = [str(a).strip() for a in raw_authors if a]
        else:
            authors = [AUTHOR_NAME]

        year = str(bib.get("pub_year") or bib.get("year") or "2020")
        venue = (bib.get("venue") or bib.get("journal") or bib.get("booktitle") or "").strip()
        abstract = (bib.get("abstract") or "").strip()
        scholar_id = pub.get("author_pub_id", "")
        citations = int(pub.get("num_citations") or 0)

        tags = auto_tag(title, abstract, venue)
        if authors and AUTHOR_NAME.lower() in authors[0].lower():
            tags.append("First Author")

        results.append({
            "title": title,
            "authors": authors,
            "date": f"{year}-01-01T00:00:00Z",
            "venue": venue,
            "abstract": abstract,
            "pub_type": infer_pub_type(venue),
            "tags": sorted(set(tags)),
            "scholar_id": scholar_id,
            "citation_count": citations,
            "featured": False,
        })

        time.sleep(0.3)
        if (i + 1) % 10 == 0:
            log.info(f"  Processed {i + 1}/{len(pubs)}...")

    log.info(f"Successfully fetched {len(results)} publications from Scholar")
    return results


def title_matches(a: str, b: str) -> bool:
    """Fuzzy title match: exact or 30-char prefix overlap."""
    a, b = a.lower().strip(), b.lower().strip()
    if a == b:
        return True
    short = min(len(a), len(b), 40)
    return short > 20 and a[:short] == b[:short]


def merge_and_sync(scholar_pubs: list[dict], existing: dict, dry_run: bool = False):
    created = updated = 0

    for pub in scholar_pubs:
        title_key = pub["title"].lower().strip()

        # Find match in existing
        match = None
        for ex_title, ex_data in existing.items():
            if title_matches(title_key, ex_title):
                match = ex_data
                break

        if match:
            ex_fm = match["fm"]
            # Preserve existing fields, layer in Scholar metadata
            fm = dict(ex_fm)
            fm["scholar_id"] = pub["scholar_id"] or ex_fm.get("scholar_id", "")
            fm["citation_count"] = pub["citation_count"]

            # Update abstract only if current one is a placeholder
            cur_abstract = ex_fm.get("abstract", "")
            if (not cur_abstract or cur_abstract.startswith("Presented at")) and pub["abstract"]:
                fm["abstract"] = pub["abstract"]

            # Merge tags
            existing_tags = set(ex_fm.get("tags", []))
            fm["tags"] = sorted(existing_tags | set(pub["tags"]))

            write_pub_file(match["slug"], fm, match["body"], dry_run)
            log.info(f"  {'[dry] ' if dry_run else ''}Updated: {match['slug']} (citations: {pub['citation_count']})")
            updated += 1
        else:
            # New entry
            slug = slugify(pub["title"])
            base = slug
            i = 1
            while not dry_run and (CONTENT_DIR / slug).exists():
                slug = f"{base}-{i}"
                i += 1

            fm = {
                "title": pub["title"],
                "authors": pub["authors"],
                "date": pub["date"],
                "publishDate": pub["date"],
                "doi": "",
                "publication_types": [pub["pub_type"]],
                "publication": pub["venue"],
                "publication_short": pub["venue"],
                "abstract": pub["abstract"],
                "tags": pub["tags"],
                "featured": False,
                "scholar_id": pub["scholar_id"],
                "citation_count": pub["citation_count"],
            }
            write_pub_file(slug, fm, "", dry_run)
            log.info(f"  {'[dry] ' if dry_run else ''}Created: {slug}")
            created += 1

    log.info(f"Sync complete: {created} created, {updated} updated")


def export_yaml():
    """Export all publications from content/publication/ to data/publications.yaml."""
    output = []
    if not CONTENT_DIR.exists():
        log.warning("content/publication/ not found")
        return

    for pub_dir in CONTENT_DIR.iterdir():
        if not pub_dir.is_dir():
            continue
        index = pub_dir / "index.md"
        if not index.exists():
            continue
        fm, _ = parse_frontmatter(index)
        if fm.get("title"):
            output.append({"slug": pub_dir.name, **fm})

    output.sort(key=lambda x: x.get("date", ""), reverse=True)

    DATA_DIR.mkdir(exist_ok=True)
    out_path = DATA_DIR / "publications.yaml"
    with open(out_path, "w", encoding="utf-8") as f:
        yaml.dump(output, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    log.info(f"Exported {len(output)} publications → {out_path}")


def main():
    parser = argparse.ArgumentParser(description="Sync Google Scholar publications to Hugo site")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing files")
    parser.add_argument("--export-only", action="store_true", help="Only export data/publications.yaml, skip Scholar fetch")
    parser.add_argument("--no-export", action="store_true", help="Skip exporting data/publications.yaml")
    args = parser.parse_args()

    # Always run from repo root
    repo_root = Path(__file__).parent.parent
    os.chdir(repo_root)

    if args.export_only:
        export_yaml()
        return

    existing = load_existing()
    log.info(f"Loaded {len(existing)} existing publications")

    scholar_pubs = fetch_scholar_publications()

    if scholar_pubs:
        merge_and_sync(scholar_pubs, existing, dry_run=args.dry_run)
    else:
        log.warning("Scholar fetch failed or returned no results — keeping existing publications unchanged")

    if not args.no_export and not args.dry_run:
        export_yaml()


if __name__ == "__main__":
    main()
