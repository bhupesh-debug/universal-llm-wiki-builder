---
id: multi-layer-watermark-removal
type: method
status: active
created: 2026-10-21
updated: 2026-10-21
sources:
  - SRC-001
tags:
  - method
  - workflow
  - cleaning-pipeline
---

# Multi-Layer Watermark Removal Pipeline

## Purpose & Overview
This method defines the rigorous end-to-end procedure for inspecting, cleaning, rewriting, and verifying text and media assets to eliminate synthetic provenance marks while preventing data corruption.

## Prerequisites & Tooling
- Python 3.10+ standard library.
- Optional system tools: `qpdf` (PDF rebuild), `exiftool` (deep metadata strip), `c2patool` (manifest inspection).
- Optional Layer B model backend: Ollama (`llama3.2`) or OpenAI-compatible endpoint.

## Step-by-Step Procedure

```
[Input Asset]
      │
      ▼
1. Classify Format (magic bytes & extension)
      │
      ├── If Text (Markdown, TXT, Code, HTML) ──┐
      │                                         ▼
      │                     2. Layer A: Strip Invisible Unicode
      │                                         │
      │                                         ▼
      │                     3. Layer B: Detection-Guided Rewrite (MLM/Paraphrase)
      │                                         │
      │                                         ▼
      │                     4. Verification (Bigram-Jaccard / MarkLLM score)
      │
      └── If Binary / Container (PDF, Images, Audio, Video) ──┐
                                                              ▼
                                            5. Metadata Strip (EXIF/XMP/C2PA)
                                                              │
                                                              ▼
                                            6. Structural Rebuild (qpdf / container swap)
                                                              │
                                                              ▼
                                            7. Optional Pixel Denoise (CtrlRegen)
      ┌───────────────────────────────────────────────────────┘
      ▼
[Cleaned Output Asset]
```

### Phase 1: Classification & Pre-Flight Check
1. Execute `inspect_file.py <file>` to determine format kind (`text`, `image`, `container`, or `unknown`).
2. Verify binary protection: Never run text tools on compressed archive formats (`.docx`, `.pdf`) directly.

### Phase 2: Text Execution (Layer A & B)
1. **Layer A Clean**: Run `clean_text.py <file> -o <cleaned_file>` to strip zero-width characters and normalize spaces (pass `--no-normalize-spaces` for languages with typographic space rules).
2. **Layer B Rewrite**: Execute `rewrite_text.py` with selected strategy (e.g. `paraphrase@0.8,mlm@0.2`).
3. **Loop Evaluation**: Evaluate candidates against lexical divergence or MarkLLM detector until the output clears watermark thresholds.

### Phase 3: Binary & Container Execution
1. Run `clean_file.py <input> -o <output>`.
2. For PDFs: `qpdf` unpacks and restructures the object tree, dropping Adobe/C2PA XMP metadata packets without breaking PDF internal xref tables.
3. For Images: Strip C2PA chunks (`c2pa` jumbf boxes in JPEG/PNG), reset EXIF date/time stamps, and invoke CtrlRegen if pixel-domain marks exist.

### Phase 4: Output Validation
1. Run `inspect_file.py <output>` to confirm no residual suspicious flags remain.
2. Confirm file byte integrity and readability.

## Connections
- Underlying Principles: [[ai-watermarking-mechanisms]]
- Strategic Foundations: [[watermark-mitigation-strategies]]
- Primary Tool: [[watermarks-remover]]

## References
- Source: [[SRC-001]]
