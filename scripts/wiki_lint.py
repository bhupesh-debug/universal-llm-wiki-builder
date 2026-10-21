#!/usr/bin/env python3
"""
scripts/wiki_lint.py
Automated Health Check & Linter for Universal LLM Wiki Builder
"""

import os
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT_DIR / "wiki"
RAW_DIR = ROOT_DIR / "raw"
INDEX_FILE = WIKI_DIR / "index.md"
LOG_FILE = WIKI_DIR / "log.md"

WIKILINK_PATTERN = re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]')
MD_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
FRONTMATTER_PATTERN = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)


def get_all_wiki_files():
    if not WIKI_DIR.exists():
        return []
    return list(WIKI_DIR.rglob("*.md"))


def check_links_and_orphans():
    wiki_files = get_all_wiki_files()
    existing_stems = {f.stem.lower(): f for f in wiki_files}
    existing_paths = {f.resolve(): f for f in wiki_files}
    
    # Also add root files like AGENTS, README, index
    for root_file in ROOT_DIR.glob("*.md"):
        existing_stems[root_file.stem.lower()] = root_file
        existing_paths[root_file.resolve()] = root_file

    issues = []
    referenced_stems = set()

    for file_path in wiki_files:
        try:
            content = file_path.read_text(encoding="utf-8")
        except Exception as e:
            issues.append(("CRITICAL", str(file_path), f"Cannot read file: {e}"))
            continue

        # Check frontmatter (except index.md and log.md)
        if file_path.name not in ["index.md", "log.md"]:
            fm_match = FRONTMATTER_PATTERN.match(content)
            if not fm_match:
                issues.append(("MEDIUM", str(file_path.relative_to(ROOT_DIR)), "Missing YAML frontmatter block (---)"))
            else:
                fm_text = fm_match.group(1)
                if "type:" not in fm_text:
                    issues.append(("LOW", str(file_path.relative_to(ROOT_DIR)), "Frontmatter missing 'type' field"))

        # Check wikilinks [[Page_Name]]
        for match in WIKILINK_PATTERN.finditer(content):
            target = match.group(1).strip()
            # Remove directory prefixes if present e.g. wiki/concepts/Foo -> Foo
            target_name = Path(target).name
            clean_stem = target_name.replace(".md", "").lower()
            referenced_stems.add(clean_stem)

            if clean_stem not in existing_stems:
                issues.append(("HIGH", str(file_path.relative_to(ROOT_DIR)), f"Broken wikilink: [[{target}]]"))

        # Check standard markdown relative links
        for match in MD_LINK_PATTERN.finditer(content):
            link_target = match.group(2).strip()
            if link_target.startswith("http://") or link_target.startswith("https://") or link_target.startswith("#") or link_target.startswith("mailto:"):
                continue
            # Strip anchors
            clean_target = link_target.split("#")[0].strip()
            if not clean_target:
                continue
            resolved_target = (file_path.parent / clean_target).resolve()
            if not resolved_target.exists():
                issues.append(("HIGH", str(file_path.relative_to(ROOT_DIR)), f"Broken relative link: {link_target}"))

    # Check for orphan pages (pages not referenced anywhere and not in index.md)
    index_content = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else ""
    for file_path in wiki_files:
        if file_path.name in ["index.md", "log.md", "overview.md"]:
            continue
        stem = file_path.stem.lower()
        if stem not in referenced_stems and file_path.name not in index_content:
            issues.append(("MEDIUM", str(file_path.relative_to(ROOT_DIR)), "Orphan page: not referenced in any wiki page or index.md"))

    return issues


def run_lint():
    print(f"=== Running Wiki Lint on {ROOT_DIR} ===")
    issues = check_links_and_orphans()
    
    if not issues:
        print("[PASSED] All wiki links, schemas, and references are valid! No issues found.")
        return 0

    critical_count = 0
    high_count = 0
    for severity, file_name, msg in issues:
        print(f"[{severity}] {file_name}: {msg}")
        if severity == "CRITICAL":
            critical_count += 1
        elif severity == "HIGH":
            high_count += 1

    print("\n--- Summary ---")
    print(f"Total findings: {len(issues)} (Critical: {critical_count}, High: {high_count})")
    
    return 1 if (critical_count > 0 or high_count > 0) else 0


if __name__ == "__main__":
    sys.exit(run_lint())
