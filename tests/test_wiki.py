"""
tests/test_wiki.py
Automated Acceptance Tests for Universal LLM Wiki Builder
"""

import unittest
from pathlib import Path
import re

ROOT_DIR = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT_DIR / "wiki"
RAW_DIR = ROOT_DIR / "raw"
TEMPLATES_DIR = ROOT_DIR / "templates"
INDEX_FILE = WIKI_DIR / "index.md"
LOG_FILE = WIKI_DIR / "log.md"
AGENTS_FILE = ROOT_DIR / "AGENTS.md"


class TestWikiArchitecture(unittest.TestCase):
    def test_core_directories_exist(self):
        """Verify the 4-layer directory hierarchy exists."""
        self.assertTrue(RAW_DIR.exists(), "raw/ directory must exist")
        self.assertTrue(WIKI_DIR.exists(), "wiki/ directory must exist")
        self.assertTrue(TEMPLATES_DIR.exists(), "templates/ directory must exist")
        self.assertTrue((ROOT_DIR / "scripts").exists(), "scripts/ directory must exist")
        self.assertTrue((ROOT_DIR / "tests").exists(), "tests/ directory must exist")

    def test_core_subdirectories_exist(self):
        """Verify raw and wiki subdirectories exist."""
        for sub in ["documents", "research", "web-clips", "assets"]:
            self.assertTrue((RAW_DIR / sub).exists(), f"raw/{sub} must exist")
        
        for sub in ["concepts", "entities", "methods", "comparisons", "questions", "syntheses", "sources"]:
            self.assertTrue((WIKI_DIR / sub).exists(), f"wiki/{sub} must exist")

    def test_governance_files_exist(self):
        """Verify AGENTS.md, index.md, and log.md exist."""
        self.assertTrue(AGENTS_FILE.exists(), "AGENTS.md must exist")
        self.assertTrue(INDEX_FILE.exists(), "wiki/index.md must exist")
        self.assertTrue(LOG_FILE.exists(), "wiki/log.md must exist")

    def test_templates_exist(self):
        """Verify all standard templates exist."""
        required_templates = [
            "concept.md", "entity.md", "method.md",
            "comparison.md", "question.md", "synthesis.md", "source.md"
        ]
        for tmpl in required_templates:
            tmpl_path = TEMPLATES_DIR / tmpl
            self.assertTrue(tmpl_path.exists(), f"Template {tmpl} must exist")
            content = tmpl_path.read_text(encoding="utf-8")
            self.assertTrue(content.startswith("---"), f"Template {tmpl} must contain YAML frontmatter")

    def test_log_audit_trail_validity(self):
        """Verify log.md contains formatted entries."""
        content = LOG_FILE.read_text(encoding="utf-8")
        entry_pattern = re.compile(r'##\s*\[\d{4}-\d{2}-\d{2}\]\s+\w+\s*\|')
        self.assertTrue(bool(entry_pattern.search(content)), "log.md must contain valid timestamped audit entries")

    def test_link_integrity_via_linter(self):
        """Run internal link check on wiki markdown files."""
        from scripts.wiki_lint import check_links_and_orphans
        issues = check_links_and_orphans()
        critical_or_high = [issue for issue in issues if issue[0] in ("CRITICAL", "HIGH")]
        self.assertEqual(len(critical_or_high), 0, f"Lint found critical/high issues: {critical_or_high}")


if __name__ == "__main__":
    unittest.main()
