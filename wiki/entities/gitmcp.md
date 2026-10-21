---
id: gitmcp
type: entity
status: active
created: 2026-10-21
updated: 2026-10-21
sources:
  - SRC-002
tags:
  - entity
  - mcp
  - infrastructure
---

# GitMCP

## Overview
GitMCP is a hosted infrastructure service created by Ido Sal (`idosal/git-mcp`) that automatically turns any public GitHub repository into a remote Model Context Protocol (MCP) server.

## Key Capabilities
- **URL-Based Provisioning**: Given any repository URL format `https://gitmcp.io/{owner}/{repo}`, it dynamically indexes and exposes documentation, code trees, and repository context via MCP.
- **Protocol Flexibility**: Supports Server-Sent Events (SSE) and HTTP Remote transport.
- **Client Support**: Out-of-the-box support for Claude Desktop, Cursor, Windsurf, VSCode, Cline, Highlight AI, and Msty Studio.
- **Zero Local Footprint**: Eliminates the need to clone or install local dependencies just to read tool documentation.

## Role in the AI Tooling Ecosystem
GitMCP enables AI coding agents to dynamically consume up-to-date documentation and API contracts without relying on stale pre-training data or manual web scraping.

## Connections
- Provided Endpoint: [[SRC-002]]
- Target Entity Documented: [[watermarks-remover]]
- Integration Protocol: [[mcp-agent-integration]]

## References
- Source: [[SRC-002]]
