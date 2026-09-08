# Technology Stack

**Analysis Date:** 2026-09-05

## Languages

**Primary:**
- Python 3.12 - FastMCP server, infrastructure scripts, utility automation
- Bash - CLI wrapper, deployment orchestration, health checks

**Secondary:**
- YAML - Configuration (Docker Compose, registries, MCP config)

## Runtime

**Environment:**
- macOS 12.x+ (Apple Silicon M-series - M4, M1)
- Tailscale (network tunnel for remote device coordination)
- Docker (containerization for Neo4j, Qdrant, PostgreSQL)

**Package Manager:**
- pip (Python dependencies)
- No lockfile detected — dependencies installed directly via pip/fastmcp

## Frameworks

**Core:**
- FastMCP 4.0.3 - MCP server framework for Claude integration
- FastAPI - Webhook routing and API gateway (in `_INFRASTRUCTURE/omniroute/omniroute.py`)

**Infrastructure:**
- Docker Compose 3.8 - Service orchestration

**Utilities:**
- typer (via fractal/pyproject.toml) - CLI command framework
- plasma-wiki, rich, textual - Fractal plugin dependencies

## Key Dependencies

**Critical:**
- fastmcp >= 4.0.3 - MCP server implementation; enables Claude Code tool integration
- PyYAML - YAML parsing for registries and configuration
- neo4j - Python driver for Neo4j graph database
- httpx - Async HTTP client for OmniRoute/LiteLLM routing

**Infrastructure:**
- Docker - Container runtime for databases
- docker-compose - Service orchestration

**Optional (Fractal submodule):**
- plasma-wiki >= 1 - Wiki/knowledge base management
- rich >= 15 - Terminal UI enhancements
- textual >= 8 - TUI framework
- typer >= 0.24 - CLI command framework

## Configuration

**Environment:**
- Docker Compose environment variables defined inline in `docker-compose.yml`
- OmniRoute configuration: `_INFRASTRUCTURE/omniroute/omniroute.py` reads `GITHUB_TOKEN`, `LITELLM_API_BASE`, `NEO4J_URI`, `OMNIROUTE_LOG_LEVEL`
- Neo4j Auth: `NEO4J_AUTH` (default: neo4j/changeme — must change)
- PostgreSQL Auth: `POSTGRES_USER` / `POSTGRES_PASSWORD` (default: admin/changeme — must change)

**Build:**
- Docker Compose file: `_INFRASTRUCTURE/docker-compose.yml`
- CLI schema: `_CLI/schema.yaml` (declarative command definitions)
- FastMCP registration: `_MCP/fastmcp_server.py`

## Platform Requirements

**Development:**
- macOS 12+ (Intel or Apple Silicon)
- Docker daemon running (via colima, OrbStack, or Docker Desktop)
- Python 3.12+ (for FastMCP server; system Python 3.9.6 is insufficient)
- Tailscale installed for remote device networking

**Production:**
- Mac Studio M4 (100.87.214.70 over Tailscale) - primary database host
- LaCie 4TB external drive (`/Volumes/LaCie`) - persistent storage for Neo4j, Qdrant, PostgreSQL

**Deployment Target:**
- Local-first: Docker Compose on Mac Studio
- Remote access: Via Tailscale (SSH, web dashboards)
- No cloud deployment detected (data lives on Mac Studio external drive)

---

*Stack analysis: 2026-09-05*
