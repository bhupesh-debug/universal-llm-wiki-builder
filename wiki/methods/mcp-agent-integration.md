---
id: mcp-agent-integration
type: method
status: active
created: 2026-10-21
updated: 2026-10-21
sources:
  - SRC-001
  - SRC-002
tags:
  - method
  - mcp
  - agent-tooling
---

# MCP Agent Integration Workflow

## Purpose & Overview
How to wire an AI development harness (Claude Desktop, Cursor, Antigravity, VSCode, Windsurf) to remote and local Model Context Protocol (MCP) servers to enable automated documentation retrieval and watermark-cleaning workflows.

## Configuration Profiles

### 1. Remote Documentation via GitMCP
To enable the AI agent to query the latest API and CLI documentation for `watermarks-remover`:

- **Cursor (`~/.cursor/mcp.json`)**:
  ```json
  {
    "mcpServers": {
      "watermarks-remover Docs": {
        "url": "https://gitmcp.io/guillaumemeyer/watermarks-remover"
      }
    }
  }
  ```

- **Claude Desktop (`claude_desktop_config.json`)**:
  ```json
  {
    "mcpServers": {
      "watermarks-remover Docs": {
        "command": "npx",
        "args": ["mcp-remote", "https://gitmcp.io/guillaumemeyer/watermarks-remover"]
      }
    }
  }
  ```

- **Windsurf (`~/.codeium/windsurf/mcp_config.json`)**:
  ```json
  {
    "mcpServers": {
      "watermarks-remover Docs": {
        "serverUrl": "https://gitmcp.io/guillaumemeyer/watermarks-remover"
      }
    }
  }
  ```

### 2. Local Execution via HTTP Service
For actual file cleaning without embedding heavy Python dependencies into the agent host:
1. Start the service: `python service/scripts/server.py --host 127.0.0.1 --port 8765`.
2. Configure agent environment variable: `WATERMARKS_SERVICE_URL=http://127.0.0.1:8765`.
3. Agent invokes REST endpoints:
   - `POST /inspect` to audit files.
   - `POST /clean` to receive sanitized base64 byte streams.

## Connections
- Target Tool: [[watermarks-remover]]
- Documentation Gateway: [[gitmcp]]
- Cleaning Pipeline: [[multi-layer-watermark-removal]]

## References
- Source: [[SRC-001]]
- Source: [[SRC-002]]
