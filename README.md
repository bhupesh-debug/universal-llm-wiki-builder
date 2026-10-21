# Universal LLM Wiki Builder
### Persistent Knowledge Engineering System | Version 1.0

[![Knowledge System](https://img.shields.io/badge/Architecture-4--Layer%20Compounding%20Wiki-00f2fe?style=for-the-badge)](wiki/overview.md)
[![Schema](https://img.shields.io/badge/Schema-AGENTS.md-8b5cf6?style=for-the-badge)](AGENTS.md)
[![Tooling](https://img.shields.io/badge/Lint%20%26%20Tests-Python%203-22c55e?style=for-the-badge)](scripts/wiki_lint.py)
[![Obsidian Ready](https://img.shields.io/badge/Obsidian-Graph%20View%20Ready-a855f7?style=for-the-badge)](https://obsidian.md)

Transform **any topic into a persistent, interconnected, evidence-grounded, continuously maintained Markdown wiki**.

Unlike passive document folders or ephemeral chat summaries, this system accumulates understanding, tracks evidence, connects concepts, detects contradictions, identifies unanswered questions, and improves as new sources arrive.

**Core Principle:** Read once, synthesize carefully, preserve evidence, maintain connections, and reuse accumulated knowledge.

---

## 🏛️ System Architecture

```
Repo/
├── AGENTS.md                  # Comprehensive AI Agent Operating Manual & Schema
├── CLAUDE.md                  # Quick-reference bridge for Claude Code
├── GEMINI.md                  # Quick-reference bridge for Gemini / Antigravity
├── README.md                  # This user manual and documentation
├── index.md                   # Root catalog bridge to wiki/index.md
│
├── raw/                       # LAYER A: IMMUTABLE EVIDENCE (Agent: READ-ONLY)
│   ├── documents/             # PDFs, whitepapers, book chapters, manuals
│   ├── research/              # Academic papers, datasets, formal studies
│   ├── web-clips/             # Articles, newsletters, saved clippings
│   └── assets/                # Figures, diagrams, screenshots, audio/video
│
├── wiki/                      # LAYER B: COMPOUNDING KNOWLEDGE BASE (Agent: OWNS & MAINTAINS)
│   ├── index.md               # Master content index categorized by type
│   ├── log.md                 # Append-only chronological audit ledger
│   ├── overview.md            # System narrative and knowledge map
│   ├── concepts/              # Core definitions, mechanisms, mental models
│   ├── entities/              # Organizations, people, tools, products, standards
│   ├── methods/               # Procedures, algorithms, workflows, techniques
│   ├── comparisons/           # Trade-off matrices, Head-to-Head evaluations
│   ├── questions/             # Open questions, evidence gaps, research agendas
│   ├── syntheses/             # Cross-source conclusions, meta-analyses, playbooks
│   └── sources/               # Structured summaries of ingested raw sources (SRC-###)
│
├── templates/                 # LAYER C: STANDARDIZED MARKDOWN BLUEPRINTS
│   ├── concept.md             # Theoretical constructs and definitions
│   ├── entity.md              # Organizations, tools, products, persons
│   ├── method.md              # Step-by-step procedures and algorithms
│   ├── comparison.md          # Multi-criteria comparison matrices
│   ├── question.md            # Knowledge gaps and competing hypotheses
│   ├── synthesis.md           # Multi-source meta-frameworks
│   └── source.md              # Ingestion schema with provenance & citations
│
├── scripts/                   # LAYER D: AUTOMATED AUDIT & MAINTENANCE
│   └── wiki_lint.py           # Automated health check (broken links, orphans, schemas)
│
└── tests/                     # ACCEPTANCE TEST SUITE
    └── test_wiki.py           # Automated verification of wiki integrity
```

---

## ⚡ The Three Operational Workflows

Copy and paste these standard prompt commands directly to your AI agent (Antigravity, Claude, ChatGPT, Cursor, etc.):

### 1. Ingest a Source
Drop any file (PDF, text notes, research paper, data export) into `raw/` and prompt:
> *"I added a new document to `raw/documents/my_paper.pdf`. Please **ingest** this source per [[AGENTS|AGENTS.md]]: register as `SRC-001`, extract core claims and mechanisms, create `wiki/sources/SRC-001.md`, update affected concept and method pages in `wiki/`, update `wiki/index.md`, and log the action in `wiki/log.md`."*

### 2. Query & Synthesize
Ask questions against your accumulated knowledge base:
> *"Query the wiki: What are the primary trade-offs and empirical evidence comparing Method A and Method B? Cite specific sources from `wiki/sources/`. If this produces a reusable decision framework, file it as a new page in `wiki/syntheses/` and update the index."*

### 3. Lint & Audit
Run periodic system health checks:
> *"Run a **lint** check on the wiki: verify all internal wikilinks, check for orphan pages, ensure YAML frontmatter is consistent, and flag any unsupported claims or contradictions."*

---

## 🛠️ Automated Tooling & Testing

This repository includes a standalone Python health check and unit test suite:

### Run Wiki Linter
```bash
python scripts/wiki_lint.py
```
Checks for:
- Broken internal wikilinks (`[[...]]`) and relative Markdown links
- Orphan pages not cataloged in `wiki/index.md` or linked by other pages
- Missing or malformed YAML frontmatter (`type`, `status`, etc.)
- Missing files or broken references

### Run Automated Unit Tests
```bash
python -m unittest tests/test_wiki.py
```
Verifies directory hierarchy, schema consistency, template integrity, audit trail formatting, and link validity.

---

## 👁️ Obsidian Visualization

This repository is designed out of the box as an **Obsidian Vault**:

1. Open **Obsidian**.
2. Click **Open folder as vault** and select this directory (`C:\Users\bhupe\Downloads\Vault\Repo`).
3. Open `index.md` or `wiki/overview.md` as your home dashboard.
4. Press `Ctrl + G` to view your interactive **Graph View**, visualizing how concepts, methods, entities, and sources interconnect in real time.

---

## 📋 Acceptance Criteria Checklist

- [x] 4-layer decoupled directory architecture (`raw/`, `wiki/`, `templates/`, `scripts/`, `tests/`)
- [x] Authoritative `AGENTS.md` operating manual covering all 16 specification sections
- [x] Agent bridge files (`CLAUDE.md`, `GEMINI.md`)
- [x] 7 standardized templates (`concept`, `entity`, `method`, `comparison`, `question`, `synthesis`, `source`)
- [x] Dynamic master content catalog (`wiki/index.md`) and navigation entry point (`wiki/overview.md`)
- [x] Append-only audit ledger (`wiki/log.md`) initialized with system bootstrap record
- [x] Automated linter (`scripts/wiki_lint.py`) and test suite (`tests/test_wiki.py`)
- [x] Standalone Git version control with production `.gitignore`
