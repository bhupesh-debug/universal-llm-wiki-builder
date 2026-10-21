# Raw Clip: guillaumemeyer/watermarks-remover
- **Source URL**: https://github.com/guillaumemeyer/watermarks-remover
- **Raw README URL**: https://raw.githubusercontent.com/guillaumemeyer/watermarks-remover/main/README.md
- **Retrieved**: 2026-10-21
- **Release**: v0.7.0
- **Summary**: Agent skill + stdlib Python service to strip multi-vendor AI provenance marks from text and files — for privacy and hygiene on content you own.

### Architecture Summary:
- **Layer A**: Invisible Unicode, exotic spaces, bidi, tag chars via deterministic Python scripts (`clean_text.py`, `inspect_text.py`).
- **Layer B**: Statistical (token-sampling) text watermarks (KGW / Kirchenbauer, keyed-Gumbel / Aaronson EXP, SynthID-Text) via iterative rewriting with MLM (RoBERTa) and LLM paraphrasing (`rewrite_text.py`).
- **File Metadata**: C2PA / EXIF / XMP / doc properties stripped across PNG, JPEG, WebP, AVIF, HEIC, PDF (via `qpdf` and `exiftool`), DOCX, XLSX, PPTX, EPUB, ODT, HTML, Markdown, MP4, WAV, MP3, FLAC.
- **Pixel-domain**: CtrlRegen (ControlNet + DINOv2 IP-Adapter controllable regeneration) and reverse-SynthID scoring sidecar (`aloshdenny/reverse-SynthID`).
- **Delivery**: Thin agent skill for Claude Code, Cursor, Codex, Grok, and Cowork calling a local stdlib HTTP server on port 8765 (`service/scripts/server.py`). PostToolUse hook for deterministic file cleaning.
