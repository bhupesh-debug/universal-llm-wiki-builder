---
id: statistical-watermark-removal-in-code
type: question
status: open
created: 2026-10-21
updated: 2026-10-21
sources:
  - SRC-001
tags:
  - question
  - research-gap
  - code-generation
---

# Statistical Watermark Removal in Source Code

## Question Statement
How can statistical and token-sampling watermarks (e.g. Kirchenbauer green-lists, Gumbel-Aaronson) be reliably mitigated in machine-generated programming source code without altering syntax semantics or introducing subtle software bugs?

## Why this matters
While Layer B rewriting (LLM paraphrasing and Masked Language Modeling) works effectively for natural language prose, code is highly brittle. Arbitrary variable renaming, syntactic reordering, or token substitution can violate type constraints, break test suites, or degrade performance.

## Current partial evidence & competing hypotheses
- **Hypothesis 1 (AST-Preserving Refactoring)**: Paraphrasing should be guided by Abstract Syntax Tree (AST) mutations (e.g. converting `for` loops to comprehensions, reordering independent assignments) rather than unrestricted natural language models.
- **Hypothesis 2 (Token Identifier Perturbation)**: Watermarks concentrated in variable naming can be broken by standard linter/formatter variable normalization.

## Evidence needed to resolve
Benchmark evaluation running statistical watermark detectors against Python and TypeScript repositories before and after AST-guided canonicalization.

## Connections
- Underlying Mechanisms: [[ai-watermarking-mechanisms]]
- Mitigation Pipeline: [[multi-layer-watermark-removal]]
- Primary Tool: [[watermarks-remover]]
