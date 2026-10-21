# Master Knowledge Index

Welcome to the central content catalog for this knowledge system. This index is dynamically maintained by the LLM Agent whenever pages are created, modified, or retired.

> **System Overview**: See [[wiki/overview|Knowledge System Overview]]  
> **Activity Log**: See [[wiki/log|Activity & Audit Log]]  
> **Operating Protocol**: See [[AGENTS|AGENTS.md]]

---

## 📚 Concepts (`wiki/concepts/`)
*Fundamental principles, theoretical constructs, mental models, and mechanisms.*

| Concept | Status | Last Updated | Sources | Summary |
| :--- | :--- | :--- | :--- | :--- |
| [[ai-watermarking-mechanisms]] | Active | 2026-10-21 | [[SRC-001]] | Taxonomy of syntactic, statistical, container, and pixel-domain AI watermarks. |
| [[watermark-mitigation-strategies]] | Active | 2026-10-21 | [[SRC-001]] | Defense-in-depth countermeasures across deterministic, iterative, and structural tiers. |

---

## 🏛️ Entities (`wiki/entities/`)
*Organizations, notable individuals, tools, software packages, standards, and benchmarks.*

| Entity | Status | Last Updated | Sources | Summary |
| :--- | :--- | :--- | :--- | :--- |
| [[watermarks-remover]] | Active | 2026-10-21 | [[SRC-001]], [[SRC-002]] | Privacy-first CLI/HTTP service by Guillaume Meyer stripping multi-vendor AI marks. |
| [[gitmcp]] | Active | 2026-10-21 | [[SRC-002]] | Hosted infrastructure by Ido Sal turning GitHub repositories into instant MCP endpoints. |

---

## ⚙️ Methods (`wiki/methods/`)
*Actionable procedures, algorithms, workflows, protocols, and step-by-step techniques.*

| Method | Status | Last Updated | Sources | Summary |
| :--- | :--- | :--- | :--- | :--- |
| [[multi-layer-watermark-removal]] | Active | 2026-10-21 | [[SRC-001]] | Step-by-step pipeline for file classification, Layer A/B cleaning, and structural rebuilding. |
| [[mcp-agent-integration]] | Active | 2026-10-21 | [[SRC-001]], [[SRC-002]] | Procedures for wiring AI development harnesses (Claude/Cursor) to MCP doc servers. |

---

## ⚖️ Comparisons (`wiki/comparisons/`)
*Head-to-head evaluations, multi-criteria trade-off matrices, and selection rubrics.*

| Comparison | Status | Last Updated | Sources | Summary |
| :--- | :--- | :--- | :--- | :--- |
| [[layer-a-vs-layer-b-text-cleaning]] | Active | 2026-10-21 | [[SRC-001]] | Detailed trade-off analysis between deterministic regex stripping and probabilistic rewriting. |

---

## ❓ Open Questions (`wiki/questions/`)
*Unresolved research questions, evidence gaps, competing hypotheses, and future agendas.*

| Question | Status | Last Updated | Sources | Summary |
| :--- | :--- | :--- | :--- | :--- |
| [[statistical-watermark-removal-in-code]] | Open | 2026-10-21 | [[SRC-001]] | Methods to neutralize statistical watermarks in source code without syntax or logic bugs. |

---

## 🧩 Syntheses (`wiki/syntheses/`)
*Cross-source conclusions, evolving rules of engagement, and meta-analytic frameworks.*

| Synthesis | Status | Last Updated | Sources | Summary |
| :--- | :--- | :--- | :--- | :--- |
| [[ai-provenance-and-privacy-playbook]] | Active | 2026-10-21 | [[SRC-001]], [[SRC-002]] | Operational rules of engagement and ethical governance for content privacy & hygiene. |

---

## 📑 Ingested Sources (`wiki/sources/`)
*Registered, immutable primary and secondary sources with checksums and provenance.*

| Source ID | Title | Author | Date | Scope / Type | Page Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `SRC-001` | watermarks-remover | Guillaume Meyer | 2026-10-15 | GitHub Repository (v0.7.0) | [[SRC-001]] |
| `SRC-002` | GitMCP Documentation Server | Ido Sal (GitMCP) | 2026-10-20 | Remote MCP / Web Service | [[SRC-002]] |
