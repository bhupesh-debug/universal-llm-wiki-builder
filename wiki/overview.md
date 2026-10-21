---
id: system-overview
type: overview
status: active
created: 2026-10-21
updated: 2026-10-21
tags:
  - wiki-system
  - meta
---

# Knowledge System Overview

Welcome to the **Persistent Knowledge Engineering Wiki**.

This repository is an interconnected, evidence-grounded knowledge system designed to accumulate understanding, track evidence, connect concepts, detect contradictions, and improve continuously as new sources arrive.

---

## 🏛️ Architecture & Knowledge Layers

The system strictly decouples raw evidence from derived knowledge across four layers:

```
┌────────────────────────────────────────────────────────┐
│ Layer A: Raw Sources (`raw/`)                          │
│  - Immutable evidence (documents, research, clips)      │
│  - Agent has READ-ONLY access                          │
└──────────────────────────┬─────────────────────────────┘
                           │ 8-Step Ingestion Pipeline
                           ▼
┌────────────────────────────────────────────────────────┐
│ Layer B: Compounding Wiki (`wiki/`)                    │
│  - Concepts, Entities, Methods, Comparisons            │
│  - Syntheses, Questions, Source distillations          │
│  - Agent OWNS and MAINTAINS with bidirectional links   │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Layer C: Schema & Operating Rules (`AGENTS.md`)        │
│  - Strict formatting standards & validation rubrics    │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ Layer D: Index & Audit Trail (`index.md`, `log.md`)    │
│  - Content catalog & append-only chronological ledger  │
└────────────────────────────────────────────────────────┘
```

---

## 📂 Navigation Guide

- **[[wiki/index|Master Index]]**: Browse all knowledge artifacts categorized by type.
- **[[wiki/log|Audit Ledger]]**: Chronological audit trail of all ingestion, query, and maintenance actions.
- **`raw/`**: Drop your source files (PDFs, research papers, notes, web clips) here for the LLM to ingest.
- **`templates/`**: Standard markdown blueprints ensuring structural uniformity across all wiki pages.
- **`scripts/`**: Automated health check (`scripts/wiki_lint.py`) to prevent link breakage and schema rot.

---

## 🔁 The Three Operational Workflows

### 1. Ingest
Drop a new file into `raw/` and instruct your LLM:
> *"Ingest `raw/documents/my_paper.pdf`: register as SRC-001, extract findings, create the source page, update affected concepts and methods, update index.md, and record in log.md."*

### 2. Query & Synthesize
Ask questions against your accumulated knowledge:
> *"Query the wiki: What are the main trade-offs between [Concept A] and [Concept B] based on our ingested sources? If this yields a novel framework, save it to `wiki/syntheses/`."*

### 3. Lint & Audit
Run a system health check:
> *"Run a wiki lint check: identify broken links, orphan pages, missing frontmatter, and any unreferenced claims."*
