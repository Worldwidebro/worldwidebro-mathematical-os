# Gemini CLI Resources — Complete Guide

## 📚 Awesome Lists (Start Here)

**1. [awesome-gemini-cli](https://github.com/Piebald-AI/awesome-gemini-cli)**
- Curated list of tools, extensions, and resources
- Best starting point for discovering what's available

**2. [awesome-gemini-cli (dtunai)](https://github.com/dtunai/awesome-gemini-cli)**
- Comprehensive collection with tutorials and examples

**3. [awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents)**
- Compares Gemini CLI with Claude Code, Codex CLI, etc.

---

## 🍳 Cookbooks (Hands-On Tutorials)

**4. [Gemini API Cookbook](https://github.com/google-gemini/cookbook)**
- Official Google cookbook for Gemini API
- Structured learning path with practical examples

**5. [Gemini CLI Demo Cookbook](https://github.com/ptone/cli-demo-cookbook)**
- Showcase of Gemini CLI features and use cases
- Practical demos for common workflows

---

## 💡 Best Practices & Tips

**6. [gemini-cli-tips](https://github.com/addyosmani/gemini-cli-tips)**
- ~30 pro-tips for effective Gemini CLI usage
- Covers agentic coding patterns

**7. [gemini-cli-best-practice](https://github.com/shanraisshan/gemini-cli-best-practice)**
- From "vibe coding" to structured workflows
- GEMINI.md implementation examples

**8. [Official Best Practices](https://geminicli.com/docs/extensions/best-practices/)**
- Extension development best practices
- GEMINI.md guidance

**9. [10 Pro Tips (Dev.to)](https://dev.to/proflead/gemini-cli-best-practices-10-pro-tips-youre-not-using-272b)**
- Practical tips like "Always open project folder first"
- "Ask for a plan before changes"

---

## 📝 System Prompts

**10. [Official System Prompt](https://github.com/google-gemini/gemini-cli/blob/main/packages/core/src/core/prompts.ts)**
- The actual TypeScript source of Gemini CLI's system prompt
- See what instructions the model receives

**11. [System Prompt Override (GEMINI_SYSTEM_MD)](https://geminicli.com/docs/cli/system-prompt/)**
- How to replace the built-in system prompt with your own Markdown file
- Environment variable: `GEMINI_SYSTEM_MD`

**12. [System Prompt Gist](https://gist.github.com/chigkim/9547badac809e356b0ed005d8a35f7c1)**
- Extracted system prompt for reference

**13. [Personal GEMINI.md Example](https://gist.github.com/ksprashu/6ff099d07eea9b768631a230a7527a52)**
- Real-world GEMINI.md configuration

---

## 🎯 Skills (Agent Capabilities)

**14. [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills)**
- Official skills for Gemini API, SDK, and model/agent interactions
- Lightweight technique for adding context to agents

**15. [agent-skills (Addy Osmani)](https://github.com/addyosmani/agent-skills/blob/main/docs/gemini-cli-setup.md)**
- Gemini CLI native skills system
- Auto-discovers `SKILL.md` files in `.gemini/skills/` or `.agents/skills/`

**16. [gemini-cli-skills topic](https://github.com/topics/gemini-cli-skills)**
- Collection of specialized skills for software engineering workflows

**17. [1,500+ Agent Skills Library](https://github.com/topics/gemini-skills)**
- Installable library for Claude Code, Cursor, Codex CLI, Gemini CLI
- Specialized plugins and skills

**18. [How to Create Agent Skills (Google Codelabs)](https://codelabs.developers.google.com/gemini-cli/how-to-create-agent-skills-for-gemini-cli)**
- Step-by-step tutorial on creating custom skills

**18b. [agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)**
- Curated collection of agentic skills and extensions
- Extends developer capabilities for autonomous agents

---

## 🔌 MCP Tools (Model Context Protocol)

**19. [gemini-cli-mcp-openai-bridge](https://github.com/Intelligent-Internet/gemini-cli-mcp-openai-bridge)**
- Exposes Gemini CLI tools through MCP protocol
- Acts as MCP hub connecting external tools

**20. [gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool)**
- Simple MCP server for AI assistants to interact with Gemini CLI

**21. [mcp-toolbox](https://github.com/gemini-cli-extensions/mcp-toolbox)**
- Create custom MCP servers with reliable tools
- Official extension for MCP integration

**22. [MCP Setup Tutorial](https://geminicli.com/docs/cli/tutorials/mcp-setup/)**
- How to extend Gemini CLI with MCP servers
- Example: GitHub MCP server integration

**23. [Docker MCP Toolkit](https://www.docker.com/blog/how-to-set-up-gemini-cli-with-mcp-toolkit/)**
- Set up Gemini CLI with MCP using Docker
- GitHub MCP server example

---

## 🧩 Extensions (Official & Community)

**24. [gemini-cli-extensions org](https://github.com/gemini-cli-extensions)**
- Official extensions organization
- Includes workspace, conductor, code-review, etc.

**25. [workspace extension](https://github.com/gemini-cli-extensions/workspace)**
- Google Workspace integration (Docs, Sheets, etc.)

**26. [conductor extension](https://github.com/gemini-cli-extensions/conductor)**
- Context-Driven Development
- Turns Gemini CLI into proactive project manager

**27. [code-review extension](https://github.com/gemini-cli-extensions/code-review)**
- Enhanced code quality reviews
- Adds new commands for code review workflows

**28. [philschmid's extensions](https://github.com/philschmid/gemini-cli-extension)**
- Personal collection of extensions, commands, and settings
- Includes cheat sheet

**29. [Browse All Extensions](https://geminicli.com/extensions/)**
- Official extension directory
- Includes tools for background execution, sleep/wake, etc.

---

## 💰 Token Reduction & Cost Optimization

**30. [Token Caching (Official)](https://google-gemini.github.io/gemini-cli/docs/cli/token-caching.html)**
- Automatic token caching for API key authentication
- Reuses previous context to reduce costs

**31. [rtk (Token Reduction Toolkit)](https://github.com/rtk-airtk)**
- CLI proxy that reduces LLM token usage by 60-90%
- Declarative YAML filters for Claude Code, Cursor, Copilot, Gemini

**32. [Token Optimization Topic](https://github.com/topics/token-optimization)**
- Various tools for token optimization
- Includes Go-based CLI proxy

**33. [Token Optimizer (Rust)](https://github.com/topics/token-optimization?l=rust&o=desc&s=forks)**
- Compresses shell outputs via PreToolUse hook
- Tracks USD savings in TUI dashboard

**34. [Context Management Guide](https://datalakehousehub.com/blog/2026-03-context-management-gemini-cli)**
- Complete guide to context management strategies
- Memory best practices

---

## 🤖 GitHub Actions (CI/CD Integration)

**35. [run-gemini-cli](https://github.com/google-github-actions/run-gemini-cli)**
- Official GitHub Action for Gemini CLI
- Autonomous agent for issue triage, PR reviews, code analysis

**36. [GitHub Actions Announcement](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-cli-github-actions/)**
- No-cost AI coding teammate for repositories
- Acts as autonomous agent for critical tasks

**37. [PR Review Example](https://github.com/google-github-actions/run-gemini-cli/blob/main/examples/workflows/pr-review/gemini-review.yml)**
- Example workflow for automated PR reviews

---

## 📖 Official Documentation

**38. [gemini-cli main repo](https://github.com/google-gemini/gemini-cli)**
- Official repository
- 106k+ stars

**39. [Get Started Guide](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/index.md)**
- Installation, configuration, quickstart

**40. [GEMINI.md Example](https://github.com/google-gemini/gemini-cli/blob/main/GEMINI.md)**
- Official GEMINI.md from the repo itself
- Shows purpose and configuration

**41. [Google Codelabs - Extensions](https://codelabs.developers.google.com/getting-started-gemini-cli-extensions)**
- Getting started with Gemini CLI extensions
- Self-contained packages for enhanced functionality

---

## 🦜 LangGraph Ecosystem

**42. [LangGraph Overview & Docs](https://docs.langchain.com/oss/python/langgraph/overview)**
- Official overview and quickstart guides for LangGraph

**43. [Deep Agents Overview & Quickstart](https://docs.langchain.com/oss/python/deepagents/overview)**
- Quickstart guide for Deep Agents integration

**44. [LangChain Overview](https://docs.langchain.com/oss/python/langchain/overview)**
- LangChain architecture and developer resources

**45. [LangSmith Overview](https://docs.langchain.com/langsmith/home)**
- Observability and evaluation platform for LLM applications

**46. [Unified Reference Home](https://reference.langchain.com/)**
- API reference home for LangChain ecosystem components

**47. [LangGraph Python API Reference](https://reference.langchain.com/python/langgraph)**
- Technical reference for LangGraph Python classes and methods

**48. [Deep Agents API Reference](https://reference.langchain.com/python/deepagents)**
- Technical reference for Deep Agents classes and APIs

**49. [LangChain Python API Reference](https://reference.langchain.com/python/langchain)**
- Detailed Python reference for the core LangChain SDK

**50. [LangSmith SDK / Integration Docs](https://docs.langchain.com/langsmith/observability)**
- SDK integration and setup guides for LangSmith

**51. [GitHub - LangGraph](https://github.com/langchain-ai/langgraph)**
- LangGraph source code and developer community

**52. [GitHub - Deep Agents](https://github.com/langchain-ai/deepagents)**
- Deep Agents source code repository

**53. [LangChain Academy](https://academy.langchain.com/)**
- Educational courses, tutorials, and certification materials

**54. [LangSmith Deployment Guide](https://docs.langchain.com/langsmith/deployment)**
- Guides for self-hosting and deploying LangSmith in production

### Quick Setup for APIs/Tracing
For LangSmith tracing (works automatically with LangGraph/Deep Agents):
```bash
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=lsv2_...   # Get key from https://smith.langchain.com
```

