# CLAUDE.md

This repository operates under the **Universal LLM Wiki Builder** protocol (Version 1.0) for persistent knowledge engineering.

Please read and strictly follow the operating schema, directory architecture, 8-step source ingestion pipeline, query engine rules, and acceptance tests defined in:
[[AGENTS|AGENTS.md]]

### Quick Reference:
- **`raw/`**: Read-only, immutable source documents (PDFs, papers, web clips, assets). Never rewrite or delete originals.
- **`wiki/`**: Persistent, cross-referenced compounding knowledge layer maintained by the agent.
- **`wiki/index.md`**: Master catalog of all wiki pages. Keep synchronized after every change.
- **`wiki/log.md`**: Append-only chronological audit ledger (`## [YYYY-MM-DD] <operation> | <Title>`).
- **`scripts/wiki_lint.py`**: Automated health check for broken links, orphan pages, and schema consistency.
- **Primary Goal**: Read once, synthesize carefully, preserve evidence, maintain connections, and reuse accumulated knowledge.
