# Activity & Audit Log

This chronological, append-only log tracks all modifications, ingestions, queries, and maintenance operations performed within this knowledge system.

---

## [2026-10-21] ingest | SRC-001 & SRC-002: AI Watermark Removal & GitMCP
- **Source**: 
  - `SRC-001`: Guillaume Meyer, *watermarks-remover* ([GitHub](https://github.com/guillaumemeyer/watermarks-remover), v0.7.0).
  - `SRC-002`: Ido Sal, *GitMCP Documentation Server* ([gitmcp.io](https://gitmcp.io/guillaumemeyer/watermarks-remover)).
- **Raw Evidence Stored**:
  - `raw/web-clips/SRC-001_watermarks-remover-github.md`
  - `raw/web-clips/SRC-002_watermarks-remover-gitmcp.md`
- **Pages created**:
  - `wiki/sources/SRC-001.md`: Technical distillation of `watermarks-remover` architecture.
  - `wiki/sources/SRC-002.md`: Model Context Protocol integration documentation.
  - `wiki/concepts/ai-watermarking-mechanisms.md`: Syntactic, statistical, C2PA, and spectral watermark mechanisms.
  - `wiki/concepts/watermark-mitigation-strategies.md`: Layer A/B defense-in-depth countermeasures.
  - `wiki/entities/watermarks-remover.md`: Profile of the CLI, HTTP service, and hooks.
  - `wiki/entities/gitmcp.md`: Profile of GitMCP infrastructure.
  - `wiki/methods/multi-layer-watermark-removal.md`: Operational cleaning pipeline.
  - `wiki/methods/mcp-agent-integration.md`: AI assistant wiring guide.
  - `wiki/comparisons/layer-a-vs-layer-b-text-cleaning.md`: Deterministic stripping vs statistical rewriting.
  - `wiki/questions/statistical-watermark-removal-in-code.md`: Open research gap for code-generation hygiene.
  - `wiki/syntheses/ai-provenance-and-privacy-playbook.md`: Content ownership and privacy rules of engagement.
- **Pages updated**:
  - `wiki/index.md`: Cataloged all 11 new knowledge artifacts.
- **Contradictions**:
  - Reconciled vendor claims: Google retired the public Gemini SynthID text watermarking API in August 2026; noted in `SRC-001` that SynthID text detection is now handled via research surrogates (MarkLLM) rather than vendor oracle endpoints.
- **Validation**:
  - Automated linter executed: `python scripts/wiki_lint.py`
  - Automated unit tests executed: `python -m unittest tests/test_wiki.py`
- **Outstanding issues**:
  - Need empirical evaluation of Layer B rewriting on programming languages (logged in `statistical-watermark-removal-in-code.md`).

---

## [2026-10-21] maintenance | System Initialization & Universal Wiki Scaffolding
- **Operation**: Bootstrapping Universal LLM Wiki Builder (v1.0) architecture.
- **Source**: N/A (Repository initialization per `AGENTS.md`).
- **Pages created**:
  - `AGENTS.md` (Operational protocol, schema, and agent instructions)
  - `CLAUDE.md` / `GEMINI.md` (Agent bridge files)
  - `wiki/overview.md` (System overview and navigation entry point)
  - `wiki/index.md` (Dynamic content index)
  - `wiki/log.md` (This audit ledger)
  - Standard templates: `templates/concept.md`, `templates/entity.md`, `templates/method.md`, `templates/comparison.md`, `templates/question.md`, `templates/synthesis.md`, `templates/source.md`
  - Automated tools: `scripts/wiki_lint.py`, `tests/test_wiki.py`
  - Repository documentation: `README.md`
- **Pages updated**: None (Fresh repository).
- **Contradictions**: None detected.
- **Validation**: Schema verified; directory hierarchy established (`raw/`, `wiki/`, `templates/`, `scripts/`, `tests/`).
- **Outstanding issues**: Awaiting initial source drop in `raw/` to run first end-to-end ingestion pipeline.
