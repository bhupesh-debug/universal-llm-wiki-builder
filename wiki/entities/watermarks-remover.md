---
id: watermarks-remover
type: entity
status: active
created: 2026-10-21
updated: 2026-10-21
sources:
  - SRC-001
  - SRC-002
tags:
  - entity
  - tool
  - open-source
  - python
---

# watermarks-remover

## Overview
`watermarks-remover` is an open-source, privacy-first system developed by Guillaume Meyer designed to detect and strip multi-vendor synthetic AI provenance marks, C2PA manifests, and statistical watermarks from text, documents, and media files.

## Technical Specifications
- **Author / Lead**: Guillaume Meyer (`guillaumemeyer`)
- **Language & Runtime**: Python 3.10+ (standard library only for core service)
- **Supported Hosts**: Claude Code, Codex, Cursor, Grok, Cowork, and standard terminal/Docker environments.
- **Service Endpoints**: Local HTTP server on `127.0.0.1:8765` providing `/inspect`, `/detect`, `/clean`, `/watermark`, and batch variants.
- **Supported Formats**:
  - Text: Markdown, plain text, code, HTML.
  - Documents: PDF, DOCX, XLSX, PPTX, EPUB, ODT.
  - Images: PNG, JPEG, WebP, AVIF, HEIC, BMP, GIF, TIFF, SVG.
  - Media: MP4, MOV, M4A, M4V, WAV, MP3, FLAC.
- **Repository**: [https://github.com/guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover)
- **Remote MCP Endpoint**: [[SRC-002]] (`https://gitmcp.io/guillaumemeyer/watermarks-remover`)

## Key Subsystems & Scripts
1. `service/scripts/server.py`: Standard library HTTP daemon exposing REST endpoints with OpenAPI 3.0.3 contract.
2. `service/scripts/clean_text.py`: Layer A deterministic stripping of invisible Unicode carriers.
3. `service/scripts/rewrite_text.py`: Layer B detection-guided iterative rewriting hook.
4. `service/scripts/clean_file.py`: Unified format router that orchestrates container disassembly, metadata stripping, and format-specific cleaners.
5. `service/scripts/hook_written_file.py`: Harness hook for Claude Code (`PostToolUse`) enforcing check-or-clean policies on agent-written files.

## Connections
- Implements: [[watermark-mitigation-strategies]]
- Neutralizes: [[ai-watermarking-mechanisms]]
- Primary Workflow: [[multi-layer-watermark-removal]]
- MCP Documentation Provider: [[gitmcp]]

## References
- Source: [[SRC-001]]
- Source: [[SRC-002]]
