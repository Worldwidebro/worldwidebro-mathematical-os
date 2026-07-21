// -------------------------------------------------------------
// Gemini CLI Resources Data Setup (Original Dataset)
// -------------------------------------------------------------
const resourcesData = [
  {
    id: 1,
    title: "awesome-gemini-cli",
    url: "https://github.com/Piebald-AI/awesome-gemini-cli",
    category: "Awesome Lists",
    bullets: [
      "Curated list of tools, extensions, and resources",
      "Best starting point for discovering what's available"
    ]
  },
  {
    id: 2,
    title: "awesome-gemini-cli (dtunai)",
    url: "https://github.com/dtunai/awesome-gemini-cli",
    category: "Awesome Lists",
    bullets: [
      "Comprehensive collection of resources",
      "Includes tutorials and practical examples"
    ]
  },
  {
    id: 3,
    title: "awesome-cli-coding-agents",
    url: "https://github.com/bradAGI/awesome-cli-coding-agents",
    category: "Awesome Lists",
    bullets: [
      "Compares Gemini CLI with Claude Code, Codex CLI, and others",
      "Highlights key strengths and tooling choices for developers"
    ]
  },
  {
    id: 4,
    title: "Gemini API Cookbook",
    url: "https://github.com/google-gemini/cookbook",
    category: "Cookbooks",
    bullets: [
      "Official Google cookbook for Gemini API",
      "Structured learning path with practical, interactive examples"
    ]
  },
  {
    id: 5,
    title: "Gemini CLI Demo Cookbook",
    url: "https://github.com/ptone/cli-demo-cookbook",
    category: "Cookbooks",
    bullets: [
      "Showcase of Gemini CLI features and unique use cases",
      "Practical demos optimized for common developer workflows"
    ]
  },
  {
    id: 6,
    title: "gemini-cli-tips",
    url: "https://github.com/addyosmani/gemini-cli-tips",
    category: "Best Practices",
    bullets: [
      "About 30 pro-tips for highly effective Gemini CLI usage",
      "Covers advanced agentic coding patterns and system settings"
    ]
  },
  {
    id: 7,
    title: "gemini-cli-best-practice",
    url: "https://github.com/shanraisshan/gemini-cli-best-practice",
    category: "Best Practices",
    bullets: [
      "From 'vibe coding' to highly structured workspace workflows",
      "Provides GEMINI.md implementation examples and schemas"
    ]
  },
  {
    id: 8,
    title: "Official Best Practices",
    url: "https://geminicli.com/docs/extensions/best-practices/",
    category: "Best Practices",
    bullets: [
      "Best practices for developers writing custom extensions",
      "Comprehensive GEMINI.md guidance for context loading"
    ]
  },
  {
    id: 9,
    title: "10 Pro Tips (Dev.to)",
    url: "https://dev.to/proflead/gemini-cli-best-practices-10-pro-tips-youre-not-using-272b",
    category: "Best Practices",
    bullets: [
      "Practical tips like 'Always open project folder first'",
      "Guides on 'Ask for a plan before implementing changes'"
    ]
  },
  {
    id: 10,
    title: "Official System Prompt",
    url: "https://github.com/google-gemini/gemini-cli/blob/main/packages/core/src/core/prompts.ts",
    category: "System Prompts",
    bullets: [
      "The actual TypeScript source of Gemini CLI's system prompt",
      "Look inside to see the precise rules and instructions the model receives"
    ]
  },
  {
    id: 11,
    title: "System Prompt Override (GEMINI_SYSTEM_MD)",
    url: "https://geminicli.com/docs/cli/system-prompt/",
    category: "System Prompts",
    bullets: [
      "Instructions on replacing the built-in system prompt with custom Markdown",
      "Configured easily via environment variable: GEMINI_SYSTEM_MD"
    ]
  },
  {
    id: 12,
    title: "System Prompt Gist",
    url: "https://gist.github.com/chigkim/9547badac809e356b0ed005d8a35f7c1",
    category: "System Prompts",
    bullets: [
      "Clean, extracted copy of the system prompt for reference",
      "Useful for researching model behavior and defaults"
    ]
  },
  {
    id: 13,
    title: "Personal GEMINI.md Example",
    url: "https://gist.github.com/ksprashu/6ff099d07eea9b768631a230a7527a52",
    category: "System Prompts",
    bullets: [
      "Real-world GEMINI.md configuration files",
      "Good reference for structuring project instructions"
    ]
  },
  {
    id: 14,
    title: "google-gemini/gemini-skills",
    url: "https://github.com/google-gemini/gemini-skills",
    category: "Skills",
    bullets: [
      "Official repository for Gemini API, SDK, and agent skill interactions",
      "Lightweight technique for adding contextual capability to agents"
    ]
  },
  {
    id: 15,
    title: "agent-skills (Addy Osmani)",
    url: "https://github.com/addyosmani/agent-skills/blob/main/docs/gemini-cli-setup.md",
    category: "Skills",
    bullets: [
      "Gemini CLI native skills and plugin ecosystem integration",
      "Auto-discovers SKILL.md files in .gemini/skills/ or .agents/skills/"
    ]
  },
  {
    id: 16,
    title: "gemini-cli-skills topic",
    url: "https://github.com/topics/gemini-cli-skills",
    category: "Skills",
    bullets: [
      "GitHub collection of specialized skills for engineering workflows",
      "Browse skills built by the open-source community"
    ]
  },
  {
    id: 17,
    title: "1,500+ Agent Skills Library",
    url: "https://github.com/topics/gemini-skills",
    category: "Skills",
    bullets: [
      "Installable skills shared across Claude Code, Cursor, and Gemini CLI",
      "Deep library of plugins covering languages, architectures, and testing"
    ]
  },
  {
    id: 18,
    title: "How to Create Agent Skills (Google Codelabs)",
    url: "https://codelabs.developers.google.com/gemini-cli/how-to-create-agent-skills-for-gemini-cli",
    category: "Skills",
    bullets: [
      "Official step-by-step tutorial on building custom skills",
      "Covers skill structure, JSON schemas, and command setup"
    ]
  },
  {
    id: 19,
    title: "gemini-cli-mcp-openai-bridge",
    url: "https://github.com/Intelligent-Internet/gemini-cli-mcp-openai-bridge",
    category: "MCP Tools",
    bullets: [
      "Exposes Gemini CLI tools through standard MCP protocol wrappers",
      "Acts as a central MCP hub connecting diverse external tools"
    ]
  },
  {
    id: 20,
    title: "gemini-mcp-tool",
    url: "https://github.com/jamubc/gemini-mcp-tool",
    category: "MCP Tools",
    bullets: [
      "Simple, lightweight MCP server for general AI assistant tasks",
      "Allows external AI clients to easily interact with Gemini CLI core"
    ]
  },
  {
    id: 21,
    title: "mcp-toolbox",
    url: "https://github.com/gemini-cli-extensions/mcp-toolbox",
    category: "MCP Tools",
    bullets: [
      "Quickly create custom MCP servers with secure, reliable tools",
      "Official extension designed to orchestrate MCP integrations"
    ]
  },
  {
    id: 22,
    title: "MCP Setup Tutorial",
    url: "https://geminicli.com/docs/cli/tutorials/mcp-setup/",
    category: "MCP Tools",
    bullets: [
      "Clear instructions on extending Gemini CLI with third-party MCP servers",
      "Includes an integration walk-through using the GitHub MCP server"
    ]
  },
  {
    id: 23,
    title: "Docker MCP Toolkit",
    url: "https://www.docker.com/blog/how-to-set-up-gemini-cli-with-mcp-toolkit/",
    category: "MCP Tools",
    bullets: [
      "Set up the Gemini CLI Docker environment with the MCP Toolkit",
      "Practical instructions using the GitHub MCP server with Docker"
    ]
  },
  {
    id: 24,
    title: "gemini-cli-extensions org",
    url: "https://github.com/gemini-cli-extensions",
    category: "Extensions",
    bullets: [
      "Official GitHub organization hosting extensions",
      "Includes workspace, conductor, and code-review modules"
    ]
  },
  {
    id: 25,
    title: "workspace extension",
    url: "https://github.com/gemini-cli-extensions/workspace",
    category: "Extensions",
    bullets: [
      "Google Workspace integration wrapper for Gemini CLI",
      "Access Docs, Sheets, and Drive directly through prompt actions"
    ]
  },
  {
    id: 26,
    title: "conductor extension",
    url: "https://github.com/gemini-cli-extensions/conductor",
    category: "Extensions",
    bullets: [
      "Implements Context-Driven Development pipelines",
      "Turns Gemini CLI into a proactive project manager monitoring tasks"
    ]
  },
  {
    id: 27,
    title: "code-review extension",
    url: "https://github.com/gemini-cli-extensions/code-review",
    category: "Extensions",
    bullets: [
      "Provides advanced code quality reviews directly in terminal",
      "Adds new commands specialized for Git branch PR code review workflows"
    ]
  },
  {
    id: 28,
    title: "philschmid's extensions",
    url: "https://github.com/philschmid/gemini-cli-extension",
    category: "Extensions",
    bullets: [
      "A curated personal collection of extensions, commands, and settings",
      "Includes a highly detailed developer cheat sheet"
    ]
  },
  {
    id: 29,
    title: "Browse All Extensions",
    url: "https://geminicli.com/extensions/",
    category: "Extensions",
    bullets: [
      "Official extension directory for Gemini CLI ecosystem",
      "Includes tools for background execution, sleep, and scheduling"
    ]
  },
  {
    id: 30,
    title: "Token Caching (Official)",
    url: "https://google-gemini.github.io/gemini-cli/docs/cli/token-caching.html",
    category: "Token Optimization",
    bullets: [
      "Automatic token caching when utilizing API key authentications",
      "Smart reuse of previous prompt contexts to significantly reduce run costs"
    ]
  },
  {
    id: 31,
    title: "rtk (Token Reduction Toolkit)",
    url: "https://github.com/rtk-airtk",
    category: "Token Optimization",
    bullets: [
      "CLI proxy reducing LLM token consumption by 60-90%",
      "Uses declarative YAML filters compatible with Claude Code, Cursor, Gemini"
    ]
  },
  {
    id: 32,
    title: "Token Optimization Topic",
    url: "https://github.com/topics/token-optimization",
    category: "Token Optimization",
    bullets: [
      "Collection of tools and helpers targeting token cost reduction",
      "Features a high-speed Go-based CLI proxy utility"
    ]
  },
  {
    id: 33,
    title: "Token Optimizer (Rust)",
    url: "https://github.com/topics/token-optimization?l=rust&o=desc&s=forks",
    category: "Token Optimization",
    bullets: [
      "Compresses verbose shell outputs utilizing a PreToolUse intercept hook",
      "Tracks overall USD savings reactively inside a terminal TUI dashboard"
    ]
  },
  {
    id: 34,
    title: "Context Management Guide",
    url: "https://datalakehousehub.com/blog/2026-03-context-management-gemini-cli",
    category: "Token Optimization",
    bullets: [
      "Comprehensive, in-depth guide detailing context management strategies",
      "Best practices for managing long sessions and agent memories"
    ]
  },
  {
    id: 35,
    title: "run-gemini-cli",
    url: "https://github.com/google-github-actions/run-gemini-cli",
    category: "GitHub Actions",
    bullets: [
      "Official Google GitHub Action wrapping the Gemini CLI agent",
      "Autonomous teammate for issue triage, automated PR reviews, and code analysis"
    ]
  },
  {
    id: 36,
    title: "GitHub Actions Announcement",
    url: "https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-cli-github-actions/",
    category: "GitHub Actions",
    bullets: [
      "Official announcement of the zero-cost AI teammate on GitHub",
      "Overview of how the action acts autonomously on repo issues and comments"
    ]
  },
  {
    id: 37,
    title: "PR Review Example",
    url: "https://github.com/google-github-actions/run-gemini-cli/blob/main/examples/workflows/pr-review/gemini-review.yml",
    category: "GitHub Actions",
    bullets: [
      "Ready-to-use workflow example for automated PR review integrations",
      "Demonstrates trigger configurations and comment setups"
    ]
  },
  {
    id: 38,
    title: "gemini-cli main repo",
    url: "https://github.com/google-gemini/gemini-cli",
    category: "Official Docs",
    bullets: [
      "Official GitHub repository for the Gemini CLI system",
      "Large active community with over 106,000 GitHub stars"
    ]
  },
  {
    id: 39,
    title: "Get Started Guide",
    url: "https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/index.md",
    category: "Official Docs",
    bullets: [
      "Step-by-step setup guides covering installation and credentials",
      "Fast starter commands for first-time configurations"
    ]
  },
  {
    id: 40,
    title: "GEMINI.md Example",
    url: "https://github.com/google-gemini/gemini-cli/blob/main/GEMINI.md",
    category: "Official Docs",
    bullets: [
      "The official GEMINI.md configuration script from the core repo itself",
      "Demonstrates file mapping, exclude directives, and context targets"
    ]
  },
  {
    id: 41,
    title: "Google Codelabs - Extensions",
    url: "https://codelabs.developers.google.com/getting-started-gemini-cli-extensions",
    category: "Official Docs",
    bullets: [
      "Interactive tutorial to build extensions for Gemini CLI",
      "Teaches modular programming, inputs, outputs, and MCP wrapper definitions"
    ]
  },
  {
    id: 42,
    title: "agentic-awesome-skills",
    url: "https://github.com/sickn33/agentic-awesome-skills",
    category: "Skills",
    bullets: [
      "Curated collection of agentic skills and extensions",
      "Extends developer capabilities for autonomous agents"
    ]
  },
  {
    id: 43,
    title: "LangGraph Overview & Docs",
    url: "https://docs.langchain.com/oss/python/langgraph/overview",
    category: "LangGraph",
    bullets: [
      "Official overview and quickstart guides for LangGraph",
      "Stateful, multi-actor applications with support for cyclic flows"
    ]
  },
  {
    id: 44,
    title: "Deep Agents Overview & Quickstart",
    url: "https://docs.langchain.com/oss/python/deepagents/overview",
    category: "LangGraph",
    bullets: [
      "Quickstart guide for Deep Agents integration",
      "Agentic patterns and design paradigms for LLMs"
    ]
  },
  {
    id: 45,
    title: "LangChain Overview",
    url: "https://docs.langchain.com/oss/python/langchain/overview",
    category: "LangGraph",
    bullets: [
      "LangChain architecture and developer resources",
      "Unified interface for connecting models with external data"
    ]
  },
  {
    id: 46,
    title: "LangSmith (Observability & Platform)",
    url: "https://docs.langchain.com/langsmith/home",
    category: "LangGraph",
    bullets: [
      "Observability and evaluation platform for LLM applications",
      "Trace, debug, and monitor complex chain and agent workflows"
    ]
  },
  {
    id: 47,
    title: "Unified Reference Home",
    url: "https://reference.langchain.com/",
    category: "LangGraph",
    bullets: [
      "API reference home for LangChain ecosystem components",
      "Detailed documentation of classes, methods, and configurations"
    ]
  },
  {
    id: 48,
    title: "LangGraph Python API Reference",
    url: "https://reference.langchain.com/python/langgraph",
    category: "LangGraph",
    bullets: [
      "Technical reference for LangGraph Python classes and methods",
      "Covers StateGraph, nodes, edges, compile parameters"
    ]
  },
  {
    id: 49,
    title: "Deep Agents API Reference",
    url: "https://reference.langchain.com/python/deepagents",
    category: "LangGraph",
    bullets: [
      "Technical reference for Deep Agents classes and APIs",
      "Details properties, prompts, and run configurations"
    ]
  },
  {
    id: 50,
    title: "LangChain Python API Reference",
    url: "https://reference.langchain.com/python/langchain",
    category: "LangGraph",
    bullets: [
      "Detailed Python reference for the core LangChain SDK",
      "Documentation for prompts, models, parser components"
    ]
  },
  {
    id: 51,
    title: "LangSmith SDK / Integration Docs",
    url: "https://docs.langchain.com/langsmith/observability",
    category: "LangGraph",
    bullets: [
      "SDK integration and setup guides for LangSmith",
      "Covers tracing middleware, metrics, run groups"
    ]
  },
  {
    id: 52,
    title: "GitHub - LangGraph",
    url: "https://github.com/langchain-ai/langgraph",
    category: "LangGraph",
    bullets: [
      "LangGraph source code and developer community",
      "Contribute, report issues, and view open source cycles"
    ]
  },
  {
    id: 53,
    title: "GitHub - Deep Agents",
    url: "https://github.com/langchain-ai/deepagents",
    category: "LangGraph",
    bullets: [
      "Deep Agents source code repository",
      "Browse components, examples, and integrations"
    ]
  },
  {
    id: 54,
    title: "LangChain Academy",
    url: "https://academy.langchain.com/",
    category: "LangGraph",
    bullets: [
      "Educational courses, tutorials, and certification materials",
      "Interactive learning paths for building robust agents"
    ]
  },
  {
    id: 55,
    title: "LangSmith Deployment Guide",
    url: "https://docs.langchain.com/langsmith/deployment",
    category: "LangGraph",
    bullets: [
      "Guides for self-hosting and deploying LangSmith in production",
      "Covers Kubernetes, Docker Compose, and cloud instructions"
    ]
  }
];

// -------------------------------------------------------------
// Metadata Badges Color Mapping (Gemini Guide Category Colors)
// -------------------------------------------------------------
const categoryStyles = {
  "Awesome Lists": { bg: "rgba(99, 102, 241, 0.15)", color: "var(--accent-indigo)", border: "rgba(99, 102, 241, 0.3)", accent: "#6366f1" },
  "Cookbooks": { bg: "rgba(6, 182, 212, 0.15)", color: "var(--accent-cyan)", border: "rgba(6, 182, 212, 0.3)", accent: "#06b6d4" },
  "Best Practices": { bg: "rgba(168, 85, 247, 0.15)", color: "#c084fc", border: "rgba(168, 85, 247, 0.3)", accent: "#a855f7" },
  "System Prompts": { bg: "rgba(236, 72, 153, 0.15)", color: "var(--accent-pink)", border: "rgba(236, 72, 153, 0.3)", accent: "#ec4899" },
  "Skills": { bg: "rgba(245, 158, 11, 0.15)", color: "#fbbf24", border: "rgba(245, 158, 11, 0.3)", accent: "#f59e0b" },
  "MCP Tools": { bg: "rgba(16, 185, 129, 0.15)", color: "#34d399", border: "rgba(16, 185, 129, 0.3)", accent: "#10b981" },
  "Extensions": { bg: "rgba(59, 130, 246, 0.15)", color: "#60a5fa", border: "rgba(59, 130, 246, 0.3)", accent: "#3b82f6" },
  "Token Optimization": { bg: "rgba(239, 68, 68, 0.15)", color: "#f87171", border: "rgba(239, 68, 68, 0.3)", accent: "#ef4444" },
  "GitHub Actions": { bg: "rgba(107, 114, 128, 0.2)", color: "#e5e7eb", border: "rgba(107, 114, 128, 0.3)", accent: "#9ca3af" },
  "Official Docs": { bg: "rgba(79, 70, 229, 0.18)", color: "#a5b4fc", border: "rgba(79, 70, 229, 0.35)", accent: "#4f46e5" },
  "LangGraph": { bg: "rgba(16, 185, 129, 0.15)", color: "#10b981", border: "rgba(16, 185, 129, 0.3)", accent: "#10b981" }
};

// -------------------------------------------------------------
// State Management
// -------------------------------------------------------------
let activeView = "resourcesView";
let activeCategory = "All";
let searchQuery = "";
let bookmarks = JSON.parse(localStorage.getItem("gemini_bookmarks")) || [];

// Backend Registry Datasets
let registryCapabilities = [];
let registryRepositories = [];
let registryAgents = [];
let registryIntegrations = [];
let registryFrameworks = [];
let registryModels = [];

let capabilitySearchQuery = "";
let repositorySearchQuery = "";
let agentSearchQuery = "";

// Completed File Ops Counts
let zipCount = 0;
let moveCount = 0;
let auditCount = 0;

// Course Builder Datasets
let coursesList = [];
let activePollingCourseId = null;
let pollingIntervalId = null;

// DOM Element references
const cardsGrid = document.getElementById("cardsGrid");
const searchInput = document.getElementById("searchInput");
const searchClearBtn = document.getElementById("searchClear");
const themeToggleBtn = document.getElementById("themeToggle");
const tabsContainer = document.getElementById("tabsContainer");
const totalCountEl = document.getElementById("totalCount");
const categoryCountEl = document.getElementById("categoryCount");
const bookmarksCountEl = document.getElementById("bookmarksCount");
const appHeader = document.querySelector(".app-header");
const toastEl = document.getElementById("toast");
const toastMessageEl = document.getElementById("toastMessage");

const statLabel1 = document.getElementById("statLabel1");
const statLabel2 = document.getElementById("statLabel2");
const statLabel3 = document.getElementById("statLabel3");

// -------------------------------------------------------------
// Global Navigation Panel Swapping
// -------------------------------------------------------------
document.querySelectorAll(".nav-tab").forEach(tab => {
  tab.addEventListener("click", (e) => {
    document.querySelectorAll(".nav-tab").forEach(t => {
      t.classList.remove("active");
      t.setAttribute("aria-selected", "false");
    });
    document.querySelectorAll(".view-panel").forEach(p => p.classList.remove("active"));

    tab.classList.add("active");
    tab.setAttribute("aria-selected", "true");
    
    activeView = tab.getAttribute("data-target");
    document.getElementById(activeView).classList.add("active");

    updateStatsDashboard();
  });
});

// Update top statistics panel dynamically based on active tab view
function updateStatsDashboard() {
  if (activeView === "resourcesView") {
    statLabel1.textContent = "Total Resources";
    statLabel2.textContent = "Unique Categories";
    statLabel3.textContent = "My Bookmarks";
    totalCountEl.textContent = resourcesData.length;
    categoryCountEl.textContent = Object.keys(categoryStyles).length;
    bookmarksCountEl.textContent = bookmarks.length;
  } 
  else if (activeView === "capabilitiesView") {
    statLabel1.textContent = "Total Capabilities";
    statLabel2.textContent = "Categories";
    statLabel3.textContent = "Vocabulary Size";
    totalCountEl.textContent = registryCapabilities.length;
    const categories = new Set(registryCapabilities.map(c => c.category)).size;
    categoryCountEl.textContent = categories;
    bookmarksCountEl.textContent = "25"; // Canonical standard size
  } 
  else if (activeView === "agentsView") {
    statLabel1.textContent = "Total Corporate Agents";
    statLabel2.textContent = "Unique Departments";
    statLabel3.textContent = "Target Scale";
    totalCountEl.textContent = registryAgents.length;
    const depts = new Set(registryAgents.map(a => a.category)).size;
    categoryCountEl.textContent = depts;
    bookmarksCountEl.textContent = "50+";
  }
  else if (activeView === "graphView") {
    statLabel1.textContent = "Graph Nodes";
    statLabel2.textContent = "Active Links";
    statLabel3.textContent = "Primary Paths";
    const nodeCount = new Set([
      ...registryIntegrations.map(i => i.repository),
      ...registryIntegrations.map(i => i.provides_capability),
      ...registryIntegrations.map(i => i.used_by_agent)
    ]).size;
    totalCountEl.textContent = nodeCount;
    categoryCountEl.textContent = registryIntegrations.length * 2;
    bookmarksCountEl.textContent = "3 Main";
  }
  else if (activeView === "repositoriesView") {
    statLabel1.textContent = "Total Repositories";
    statLabel2.textContent = "Sectors Covered";
    statLabel3.textContent = "Active Projects";
    const activeProjects = registryRepositories.filter(r => r.status === "active").length;
    totalCountEl.textContent = registryRepositories.length;
    categoryCountEl.textContent = "10 Layers";
    bookmarksCountEl.textContent = activeProjects;
  }
  else if (activeView === "operationsView") {
    statLabel1.textContent = "ZIP Archives Done";
    statLabel2.textContent = "Documents Moved";
    statLabel3.textContent = "Audits Run";
    totalCountEl.textContent = zipCount;
    categoryCountEl.textContent = moveCount;
    bookmarksCountEl.textContent = auditCount;
  }
  else if (activeView === "courseBuilderView") {
    statLabel1.textContent = "Courses Configured";
    statLabel2.textContent = "Total Chapters";
    statLabel3.textContent = "Materials Generated";
    totalCountEl.textContent = coursesList.length;
    let chaptersCount = coursesList.reduce((acc, c) => acc + (parseInt(c.chapters) || 0), 0);
    categoryCountEl.textContent = chaptersCount;
    bookmarksCountEl.textContent = coursesList.reduce((acc, c) => acc + (c.status === "completed" ? (parseInt(c.chapters) || 0) * 7 : 0), 0);
  }
  else if (activeView === "aipView") {
    statLabel1.textContent = "Agent Frameworks";
    statLabel2.textContent = "Available Models";
    statLabel3.textContent = "Control Tiers";
    totalCountEl.textContent = registryFrameworks.length;
    categoryCountEl.textContent = registryModels.length;
    bookmarksCountEl.textContent = "5 Tiers";
  }
}

// Fallback scroll events for old browsers
window.addEventListener("scroll", () => {
  if (!CSS.supports("(animation-timeline: scroll()) and (animation-range: 0% 100%)")) {
    if (window.scrollY > 20) {
      appHeader.classList.add("shrunk");
    } else {
      appHeader.classList.remove("shrunk");
    }
  }
});

// Setup Dark/Light Theme toggler
function initTheme() {
  const savedTheme = localStorage.getItem("gemini_theme") || "dark";
  document.documentElement.setAttribute("data-theme", savedTheme);
  updateThemeIcon(savedTheme);
}

function updateThemeIcon(theme) {
  if (theme === "light") {
    themeToggleBtn.innerHTML = `
      <svg viewBox="0 0 24 24">
        <path d="M12 7c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zM2 13h2c.55 0 1-.45 1-1s-.45-1-1-1H2c-.55 0-1 .45-1 1s.45 1 1 1zm18 0h2c.55 0 1-.45 1-1s-.45-1-1-1h-2c-.55 0-1 .45-1 1s.45 1 1 1zM11 2v2c0 .55.45 1 1 1s1-.45 1-1V2c0-.55-.45-1-1-1s-1 .45-1 1zm0 18v2c0 .55.45 1 1 1s1-.45 1-1v-2c0-.55-.45-1-1-1s-1 .45-1 1zM5.99 4.58c-.39-.39-1.03-.39-1.41 0s-.39 1.03 0 1.41l1.06 1.06c.39.39 1.03.39 1.41 0s.39-1.03 0-1.41L5.99 4.58zm12.37 12.37c-.39-.39-1.03-.39-1.41 0s-.39 1.03 0 1.41l1.06 1.06c.39.39 1.03.39 1.41 0s.39-1.03 0-1.41l-1.06-1.06zm1.06-12.37c-.39-.39-1.03-.39-1.41 0l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06c.39-.38.39-1.02 0-1.41zm-12.37 12.37c-.39-.39-1.03-.39-1.41 0l-1.06 1.06c-.39.39-.39 1.03 0 1.41s1.03.39 1.41 0l1.06-1.06c.39-.38.39-1.02 0-1.41z"/>
      </svg>`;
  } else {
    themeToggleBtn.innerHTML = `
      <svg viewBox="0 0 24 24">
        <path d="M12.3 22h-.1c-5.5 0-10-4.5-10-10 0-4.8 3.5-8.9 8.2-9.8.6-.1 1.2.3 1.3.9.1.6-.3 1.2-.9 1.3-3.6.7-6.2 3.8-6.2 7.6 0 4.4 3.6 8 8 8 3.8 0 6.9-2.6 7.6-6.2.1-.6.7-1 1.3-.9.6.1 1 .7.9 1.3-.9 4.7-5 8.2-9.8 8.2z"/>
      </svg>`;
  }
}

themeToggleBtn.addEventListener("click", () => {
  const currentTheme = document.documentElement.getAttribute("data-theme");
  const nextTheme = currentTheme === "light" ? "dark" : "light";
  document.documentElement.setAttribute("data-theme", nextTheme);
  localStorage.setItem("gemini_theme", nextTheme);
  updateThemeIcon(nextTheme);
});

// Toast notification trigger
function showToast(message) {
  toastMessageEl.textContent = message;
  toastEl.classList.add("show");
  setTimeout(() => {
    toastEl.classList.remove("show");
  }, 2500);
}

// Copy to clipboard utility
function copyTextToClipboard(text, successMsg) {
  navigator.clipboard.writeText(text).then(() => {
    showToast(successMsg);
  }).catch(() => {
    const textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.style.position = "fixed";
    document.body.appendChild(textarea);
    textarea.select();
    try {
      document.execCommand("copy");
      showToast(successMsg);
    } catch (err) {
      showToast("Failed to copy text");
    }
    document.body.removeChild(textarea);
  });
}

// -------------------------------------------------------------
// VIEW 1: Gemini CLI Guide Logic
// -------------------------------------------------------------
function renderCategoryTabs() {
  const categories = ["All", ...Object.keys(categoryStyles), "Bookmarks"];
  
  tabsContainer.innerHTML = categories.map(cat => {
    const isActive = cat === activeCategory;
    let badgeContent = "";
    
    if (cat === "All") {
      badgeContent = `<span class="badge-count">${resourcesData.length}</span>`;
    } else if (cat === "Bookmarks") {
      badgeContent = `<span class="badge-count" id="bookmarkTabBadge">${bookmarks.length}</span>`;
    } else {
      const count = resourcesData.filter(r => r.category === cat).length;
      badgeContent = `<span class="badge-count">${count}</span>`;
    }
    
    return `
      <button class="tab-btn ${isActive ? 'active' : ''}" data-category="${cat}">
        ${cat === 'Bookmarks' ? '⭐ ' : ''}${cat} ${badgeContent}
      </button>
    `;
  }).join("");
  
  const tabButtons = tabsContainer.querySelectorAll(".tab-btn");
  tabButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      tabButtons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeCategory = btn.getAttribute("data-category");
      filterAndRenderCards();
    });
  });
}

function updateBookmarkStats() {
  if (activeView === "resourcesView") {
    bookmarksCountEl.textContent = bookmarks.length;
  }
  const badge = document.getElementById("bookmarkTabBadge");
  if (badge) {
    badge.textContent = bookmarks.length;
  }
}

function toggleBookmark(id) {
  const idx = bookmarks.indexOf(id);
  if (idx > -1) {
    bookmarks.splice(idx, 1);
    showToast("Removed from Bookmarks");
  } else {
    bookmarks.push(id);
    showToast("Added to Bookmarks");
  }
  localStorage.setItem("gemini_bookmarks", JSON.stringify(bookmarks));
  updateBookmarkStats();
  
  if (activeCategory === "Bookmarks") {
    filterAndRenderCards();
  } else {
    const cardEl = document.querySelector(`.resource-card[data-id="${id}"]`);
    if (cardEl) {
      const starBtn = cardEl.querySelector(".btn-bookmark");
      if (starBtn) {
        starBtn.classList.toggle("bookmarked");
      }
    }
  }
}

function getMarkdownForCard(card) {
  let md = `**[${card.title}](${card.url})**\n`;
  card.bullets.forEach(b => {
    md += `- ${b}\n`;
  });
  return md;
}

function renderCards(dataset) {
  if (dataset.length === 0) {
    cardsGrid.innerHTML = `
      <div class="empty-state">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <h3>No resources found</h3>
        <p>Try refining your search terms or selecting a different category.</p>
      </div>`;
    return;
  }
  
  cardsGrid.innerHTML = dataset.map(item => {
    const isBookmarked = bookmarks.includes(item.id);
    const style = categoryStyles[item.category] || categoryStyles["Official Docs"];
    
    const bulletListHtml = item.bullets.map(bullet => {
      let text = bullet;
      if (searchQuery) {
        const regex = new RegExp(`(${escapeRegex(searchQuery)})`, "gi");
        text = text.replace(regex, "<mark>$1</mark>");
      }
      return `<li>${text}</li>`;
    }).join("");
    
    let highlightedTitle = item.title;
    if (searchQuery) {
      const regex = new RegExp(`(${escapeRegex(searchQuery)})`, "gi");
      highlightedTitle = highlightedTitle.replace(regex, "<mark>$1</mark>");
    }

    return `
      <div class="resource-card" data-id="${item.id}" style="
        --card-accent: ${style.accent};
        --card-accent-dot: ${style.accent};
        --badge-bg: ${style.bg};
        --badge-color: ${style.color};
        --badge-border: ${style.border};
      ">
        <div class="card-header">
          <span class="card-badge">${item.category}</span>
          <button class="btn-bookmark ${isBookmarked ? 'bookmarked' : ''}" onclick="toggleBookmark(${item.id})" aria-label="Bookmark resource">
            <svg viewBox="0 0 24 24">
              <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
            </svg>
          </button>
        </div>
        
        <div class="card-title-area">
          <span class="card-num">${item.id}</span>
          <h3 class="card-title">
            <a href="${item.url}" target="_blank" rel="noopener noreferrer">${highlightedTitle}</a>
          </h3>
        </div>
        
        <ul class="card-details">
          ${bulletListHtml}
        </ul>
        
        <div class="card-actions">
          <a class="card-btn card-btn-primary" href="${item.url}" target="_blank" rel="noopener noreferrer">
            <svg viewBox="0 0 24 24">
              <path d="M19 19H5V5h7V3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"/>
            </svg>
            Open
          </a>
          <button class="card-btn" onclick="copyLink('${item.url}')">
            <svg viewBox="0 0 24 24">
              <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
            </svg>
            Link
          </button>
          <button class="card-btn" onclick="copyMarkdown(${item.id})">
            <svg viewBox="0 0 24 24">
              <path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/>
            </svg>
            MD
          </button>
        </div>
      </div>
    `;
  }).join("");
}

function escapeRegex(string) {
  return string.replace(/[/\-\\^$*+?.()|[\]{}]/g, '\\$&');
}

function filterAndRenderCards() {
  cardsGrid.style.opacity = 0;
  
  setTimeout(() => {
    let filtered = [...resourcesData];
    
    if (activeCategory === "Bookmarks") {
      filtered = filtered.filter(item => bookmarks.includes(item.id));
    } else if (activeCategory !== "All") {
      filtered = filtered.filter(item => item.category === activeCategory);
    }
    
    if (searchQuery) {
      const q = searchQuery.toLowerCase();
      filtered = filtered.filter(item => {
        const titleMatch = item.title.toLowerCase().includes(q);
        const categoryMatch = item.category.toLowerCase().includes(q);
        const urlMatch = item.url.toLowerCase().includes(q);
        const bulletMatch = item.bullets.some(b => b.toLowerCase().includes(q));
        
        return titleMatch || categoryMatch || urlMatch || bulletMatch;
      });
    }
    
    renderCards(filtered);
    cardsGrid.style.opacity = 1;
  }, 150);
}

searchInput.addEventListener("input", (e) => {
  searchQuery = e.target.value;
  if (searchQuery.trim().length > 0) {
    searchClearBtn.style.display = "flex";
  } else {
    searchClearBtn.style.display = "none";
  }
  filterAndRenderCards();
});

searchClearBtn.addEventListener("click", () => {
  searchInput.value = "";
  searchQuery = "";
  searchClearBtn.style.display = "none";
  searchInput.focus();
  filterAndRenderCards();
});

// -------------------------------------------------------------
// VIEW 2: System Capabilities Registry Logic
// -------------------------------------------------------------
async function fetchCapabilities() {
  try {
    const res = await fetch("/api/registry/capabilities");
    if (!res.ok) throw new Error("API error fetching capabilities");
    const jsonRes = await res.json();
    registryCapabilities = jsonRes.data || [];
    renderCapabilities();
    updateStatsDashboard();
  } catch (err) {
    console.error(err);
    document.getElementById("capabilitiesContainer").innerHTML = `
      <div class="empty-state">
        <h3>Capabilities Registry Unavailable</h3>
        <p>Could not connect to backend server. Ensure server.py is running on port 8000.</p>
      </div>`;
  }
}

function renderCapabilities() {
  const container = document.getElementById("capabilitiesContainer");
  if (registryCapabilities.length === 0) return;

  let items = [...registryCapabilities];

  if (capabilitySearchQuery) {
    const q = capabilitySearchQuery.toLowerCase();
    items = items.filter(c => {
      return c.name.toLowerCase().includes(q) || 
             c.category.toLowerCase().includes(q) || 
             c.description.toLowerCase().includes(q);
    });
  }

  if (items.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <h3>No matching capabilities found</h3>
      </div>`;
    return;
  }

  container.innerHTML = items.map(c => {
    const linkedRepos = registryIntegrations
      .filter(i => i.provides_capability === c.id)
      .map(i => i.repository);

    const reposListHtml = linkedRepos.map(r => `<li>${r}</li>`).join("");

    return `
      <div class="capability-card">
        <div class="capability-header">
          <h3 class="capability-title">${c.name}</h3>
          <span class="capability-category" style="background: rgba(6, 182, 212, 0.15); color: var(--accent-cyan); border-color: rgba(6, 182, 212, 0.3);">${c.category}</span>
        </div>
        <p class="box-desc" style="margin-bottom: 12px; min-height: 38px;">${c.description}</p>
        <div class="capability-repos">
          <div class="capability-repos-title">Linked Repos (${linkedRepos.length})</div>
          <ul class="capability-repos-list">
            ${linkedRepos.length > 0 ? reposListHtml : '<li style="color: var(--text-muted); font-style: italic;">No cataloged repos</li>'}
          </ul>
        </div>
      </div>
    `;
  }).join("");
}

document.getElementById("capabilitySearchInput").addEventListener("input", (e) => {
  capabilitySearchQuery = e.target.value;
  renderCapabilities();
});

// -------------------------------------------------------------
// VIEW 3: Agent Factory Catalog Logic
// -------------------------------------------------------------
async function fetchAgents() {
  try {
    const res = await fetch("/api/registry/agents");
    if (!res.ok) throw new Error("API error fetching agents registry");
    const jsonRes = await res.json();
    registryAgents = jsonRes.data || [];
    renderAgents();
    updateStatsDashboard();
  } catch (err) {
    console.error(err);
    document.getElementById("agentsContainer").innerHTML = `
      <div class="empty-state">
        <h3>Agent Catalog Registry Unavailable</h3>
      </div>`;
  }
}

function renderAgents() {
  const container = document.getElementById("agentsContainer");
  if (registryAgents.length === 0) return;

  let items = [...registryAgents];

  if (agentSearchQuery) {
    const q = agentSearchQuery.toLowerCase();
    items = items.filter(a => {
      const nameMatch = a.name.toLowerCase().includes(q);
      const roleMatch = a.role.toLowerCase().includes(q);
      const focusMatch = a.focus.toLowerCase().includes(q);
      const categoryMatch = a.category.toLowerCase().includes(q);
      return nameMatch || roleMatch || focusMatch || categoryMatch;
    });
  }

  if (items.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <h3>No matching corporate agents found</h3>
      </div>`;
    return;
  }

  container.innerHTML = items.map(a => {
    const inputsHtml = a.inputs.map(i => `<span class="tag" style="background: rgba(239, 68, 68, 0.1); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.2);">${i}</span>`).join("");
    const outputsHtml = a.outputs.map(o => `<span class="tag" style="background: rgba(16, 185, 129, 0.1); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.2);">${o}</span>`).join("");

    return `
      <div class="capability-card" style="border-top: 4px solid var(--accent-violet);">
        <div class="capability-header">
          <h3 class="capability-title" style="color: var(--accent-violet);">${a.name}</h3>
          <span class="capability-category" style="background: rgba(124, 58, 237, 0.15); color: #c084fc; border-color: rgba(124, 58, 237, 0.3);">${a.category}</span>
        </div>
        <div style="font-size: 0.85rem; font-weight: 700; color: var(--text-muted); margin-bottom: 8px;">${a.role}</div>
        <p class="box-desc" style="line-height: 1.4; min-height: 48px;">${a.focus}</p>
        
        <div style="margin-top: 12px; border-top: 1px solid var(--border-glass); padding-top: 10px;">
          <div style="font-size: 0.72rem; font-weight: 700; color: var(--text-muted); margin-bottom: 4px; letter-spacing: 0.05em;">INPUT DATA</div>
          <div class="capability-aliases" style="margin-bottom: 8px; display: flex; flex-wrap: wrap; gap: 4px;">${inputsHtml}</div>
          
          <div style="font-size: 0.72rem; font-weight: 700; color: var(--text-muted); margin-bottom: 4px; letter-spacing: 0.05em;">OUTPUT PRODUCTS</div>
          <div class="capability-aliases" style="margin-bottom: 0; display: flex; flex-wrap: wrap; gap: 4px;">${outputsHtml}</div>
        </div>
      </div>
    `;
  }).join("");
}

document.getElementById("agentSearchInput").addEventListener("input", (e) => {
  agentSearchQuery = e.target.value;
  renderAgents();
});

// -------------------------------------------------------------
// VIEW 4: Capability Graph Visualization (SVG Render)
// -------------------------------------------------------------
async function fetchGraphData() {
  try {
    const res = await fetch("/api/graph/data");
    if (!res.ok) throw new Error("API error fetching graph integrations");
    const data = await res.json();
    registryIntegrations = data.integrations || [];
    renderGraph();
    updateStatsDashboard();
  } catch (err) {
    console.error(err);
  }
}

function renderGraph() {
  const svg = document.getElementById("capabilityGraphSvg");
  if (!svg) return;
  svg.innerHTML = "";

  const defs = document.createElementNS("http://www.w3.org/2000/svg", "defs");
  defs.innerHTML = `
    <marker id="arrow" viewBox="0 0 10 10" refX="28" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="rgba(255,255,255,0.25)" />
    </marker>
    <marker id="arrow-highlight" viewBox="0 0 10 10" refX="28" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--accent-pink)" />
    </marker>
  `;
  svg.appendChild(defs);

  // We align nodes into three distinct columns: Repos (left), Capabilities (middle), Agents (right)
  const repos = [...new Set(registryIntegrations.map(i => i.repository))];
  const caps = [...new Set(registryIntegrations.map(i => i.provides_capability))];
  const agents = [...new Set(registryIntegrations.map(i => i.used_by_agent).filter(Boolean))];

  const nodeCoords = {};

  // Render Repository Nodes (Left column, X = 130)
  const repoYOffset = 420 / (repos.length + 1);
  repos.forEach((name, idx) => {
    const y = repoYOffset * (idx + 1);
    nodeCoords[`repo-${name}`] = { x: 130, y };
    const isHighlight = ["PaddleOCR", "Qdrant", "LlamaIndex"].includes(name);
    drawNode(svg, 130, y, name, "Repository", isHighlight);
  });

  // Render Capability Nodes (Middle column, X = 450)
  const capYOffset = 420 / (caps.length + 1);
  caps.forEach((capId, idx) => {
    const y = capYOffset * (idx + 1);
    nodeCoords[`cap-${capId}`] = { x: 450, y };
    const isHighlight = ["document-extraction", "vector-search", "rag-orchestrator"].includes(capId);
    drawNode(svg, 450, y, capId, "Capability", isHighlight);
  });

  // Render Agent Nodes (Right column, X = 770)
  const agentYOffset = 420 / (agents.length + 1);
  agents.forEach((name, idx) => {
    const y = agentYOffset * (idx + 1);
    nodeCoords[`agent-${name}`] = { x: 770, y };
    const isHighlight = name === "Research Agent";
    drawNode(svg, 770, y, name, "Agent", isHighlight);
  });

  // Curved connections drawing
  registryIntegrations.forEach(i => {
    const start = nodeCoords[`repo-${i.repository}`];
    const end = nodeCoords[`cap-${i.provides_capability}`];
    
    if (start && end) {
      const isHighlight = 
        (["PaddleOCR", "Qdrant", "LlamaIndex"].includes(i.repository)) &&
        (["document-extraction", "vector-search", "rag-orchestrator"].includes(i.provides_capability));
      drawConnection(svg, start.x, start.y, end.x, end.y, isHighlight);
    }

    if (i.used_by_agent) {
      const capStart = nodeCoords[`cap-${i.provides_capability}`];
      const agentEnd = nodeCoords[`agent-${i.used_by_agent}`];
      
      if (capStart && agentEnd) {
        const isHighlight = 
          (["document-extraction", "vector-search", "rag-orchestrator"].includes(i.provides_capability)) &&
          (i.used_by_agent === "Research Agent");
        drawConnection(svg, capStart.x, capStart.y, agentEnd.x, agentEnd.y, isHighlight);
      }
    }
  });
}

function drawNode(svg, x, y, label, type, isHighlight) {
  const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
  
  const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
  rect.setAttribute("x", x - 90);
  rect.setAttribute("y", y - 18);
  rect.setAttribute("width", 180);
  rect.setAttribute("height", 36);
  rect.setAttribute("rx", 6);
  rect.setAttribute("ry", 6);
  
  let strokeColor = "var(--border-glass)";
  let fillColor = "rgba(18, 16, 38, 0.9)";
  
  if (isHighlight) {
    strokeColor = "var(--accent-pink)";
    fillColor = "rgba(236, 72, 153, 0.12)";
  } else {
    if (type === "Repository") strokeColor = "rgba(99, 102, 241, 0.35)";
    if (type === "Capability") strokeColor = "rgba(6, 182, 212, 0.35)";
    if (type === "Agent") strokeColor = "rgba(236, 72, 153, 0.35)";
  }

  rect.setAttribute("stroke", strokeColor);
  rect.setAttribute("stroke-width", isHighlight ? "2" : "1");
  rect.setAttribute("fill", fillColor);
  g.appendChild(rect);

  const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
  text.setAttribute("x", x);
  text.setAttribute("y", y + 4);
  text.setAttribute("text-anchor", "middle");
  text.setAttribute("fill", isHighlight ? "var(--accent-pink)" : "var(--text-primary)");
  text.setAttribute("style", `font-size: 0.72rem; font-family: 'Inter', sans-serif; font-weight: ${isHighlight ? '700' : '500'};`);
  text.textContent = label.length > 20 ? label.slice(0, 18) + ".." : label;
  g.appendChild(text);

  svg.appendChild(g);
}

function drawConnection(svg, x1, y1, x2, y2, isHighlight) {
  const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
  const cx1 = x1 + (x2 - x1) * 0.4;
  const cy1 = y1;
  const cx2 = x1 + (x2 - x1) * 0.6;
  const cy2 = y2;

  path.setAttribute("d", `M ${x1} ${y1} C ${cx1} ${cy1}, ${cx2} ${cy2}, ${x2} ${y2}`);
  path.setAttribute("fill", "none");
  path.setAttribute("stroke", isHighlight ? "var(--accent-pink)" : "rgba(255,255,255,0.08)");
  path.setAttribute("stroke-width", isHighlight ? "2.5" : "1.2");
  path.setAttribute("marker-end", isHighlight ? "url(#arrow-highlight)" : "url(#arrow)");
  
  if (isHighlight) {
    path.setAttribute("stroke-dasharray", "8, 5");
    const animate = document.createElementNS("http://www.w3.org/2000/svg", "animate");
    animate.setAttribute("attributeName", "stroke-dashoffset");
    animate.setAttribute("values", "100;0");
    animate.setAttribute("dur", "4s");
    animate.setAttribute("repeatCount", "indefinite");
    path.appendChild(animate);
  }

  svg.appendChild(path);
}

// -------------------------------------------------------------
// VIEW 5: Venture Repositories Table Logic
// -------------------------------------------------------------
async function fetchRepositories() {
  try {
    const res = await fetch("/api/repositories");
    if (!res.ok) throw new Error("API error fetching repositories");
    const data = await res.json();
    registryRepositories = data.repositories || [];
    renderRepositories();
    updateStatsDashboard();
  } catch (err) {
    console.error(err);
    document.getElementById("repositoriesTableBody").innerHTML = `
      <tr>
        <td colspan="5" style="text-align: center; color: var(--text-muted);">
          Repositories registry unavailable. Run server.py backend.
        </td>
      </tr>`;
  }
}

function renderRepositories() {
  const tableBody = document.getElementById("repositoriesTableBody");
  if (registryRepositories.length === 0) return;

  let filtered = [...registryRepositories];
  if (repositorySearchQuery) {
    const q = repositorySearchQuery.toLowerCase();
    filtered = filtered.filter(r => {
      return r.name.toLowerCase().includes(q) || 
             r.sector.toLowerCase().includes(q) || 
             r.status.toLowerCase().includes(q) ||
             r.venture_id.toLowerCase().includes(q);
    });
  }

  if (filtered.length === 0) {
    tableBody.innerHTML = `
      <tr>
        <td colspan="5" style="text-align: center;">No matching repositories cataloged.</td>
      </tr>`;
    return;
  }

  tableBody.innerHTML = filtered.map(r => {
    const statusClass = r.status.toLowerCase();
    return `
      <tr>
        <td class="repo-code">${r.name}</td>
        <td>${r.venture_id}</td>
        <td>${r.sector}</td>
        <td><span class="repo-badge ${statusClass}">${r.status}</span></td>
        <td>
          <button class="card-btn" onclick="quickArchive('${r.name}')" style="width: auto; padding: 4px 10px; font-size: 0.75rem;">
            ZIP
          </button>
        </td>
      </tr>
    `;
  }).join("");
}

document.getElementById("repositorySearchInput").addEventListener("input", (e) => {
  repositorySearchQuery = e.target.value;
  renderRepositories();
});

window.quickArchive = (repoName) => {
  const guessPath = `WORLDWIDEBRO-OS/03-PORTFOLIO/ventures/active/${repoName}`;
  document.getElementById("zipPath").value = guessPath;
  document.querySelector('.nav-tab[data-target="operationsView"]').click();
  showToast(`Pre-loaded archive path for ${repoName}`);
};

// -------------------------------------------------------------
// VIEW 6: File Operations & Auditing Controllers
// -------------------------------------------------------------
async function postApiRequest(endpoint, body) {
  try {
    const res = await fetch(endpoint, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(body)
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || "Server endpoint operation failed");
    return data;
  } catch (err) {
    showToast(err.message);
    throw err;
  }
}

// ZIP Action
document.getElementById("btnRunZip").addEventListener("click", async () => {
  const path = document.getElementById("zipPath").value.trim();
  if (!path) {
    showToast("Please specify a target workspace folder");
    return;
  }
  try {
    const data = await postApiRequest("/api/zip", { path });
    zipCount++;
    updateStatsDashboard();
    showToast(`Archive complete! Size: ${(data.size_bytes / (1024*1024)).toFixed(2)} MB`);
  } catch (err) {
    console.error(err);
  }
});

// MOVE Action
document.getElementById("btnRunMove").addEventListener("click", async () => {
  const src = document.getElementById("moveSrc").value.trim();
  const dest = document.getElementById("moveDest").value.trim();
  if (!src || !dest) {
    showToast("Source and destination paths are required");
    return;
  }
  try {
    await postApiRequest("/api/move", { src, dest });
    moveCount++;
    updateStatsDashboard();
    showToast("Document moved successfully");
    document.getElementById("moveSrc").value = "";
    document.getElementById("moveDest").value = "";
  } catch (err) {
    console.error(err);
  }
});

// PDF Action
document.getElementById("btnRunPdf").addEventListener("click", async () => {
  try {
    const data = await postApiRequest("/api/pdf", {});
    showToast("PDF report generated successfully!");
    console.log("PDF Created at:", data.pdf_path);
  } catch (err) {
    console.error(err);
  }
});

// COMPLIANCE AUDIT Action
document.getElementById("btnRunAudit").addEventListener("click", async () => {
  const campaign = document.getElementById("auditCampaignId").value.trim();
  if (!campaign) {
    showToast("Please enter a campaign folder name");
    return;
  }
  const consoleStatus = document.getElementById("consoleStatus");
  const consoleBody = document.getElementById("consoleBody");
  consoleStatus.textContent = "RUNNING";
  consoleStatus.className = "console-status running";
  consoleBody.textContent = `Starting compliance audit runner for campaign: '${campaign}'...\nLoading manifest...\nReading regulation guidelines...`;
  try {
    const data = await postApiRequest("/api/audit", { campaign });
    auditCount++;
    updateStatsDashboard();
    setTimeout(() => {
      if (data.status === "pass") {
        consoleStatus.textContent = "PASSED";
        consoleStatus.className = "console-status passed";
      } else {
        consoleStatus.textContent = "FAILED";
        consoleStatus.className = "console-status failed";
      }
      consoleBody.textContent = JSON.stringify(data, null, 2);
    }, 800);
  } catch (err) {
    consoleStatus.textContent = "ERROR";
    consoleStatus.className = "console-status failed";
    consoleBody.textContent = `[AUDIT RUNNER FATAL ERROR]\n${err.message}`;
  }
});

// Obsidian Sync Action
document.getElementById("btnRunObsidianSync").addEventListener("click", async () => {
  showToast("Starting Obsidian alignment sync...");
  try {
    const data = await postApiRequest("/api/execute", { capability_id: "obsidian-sync" });
    showToast("Obsidian Sync Completed!");
    console.log("Obsidian sync output:", data);
  } catch (err) {
    console.error(err);
  }
});

// Graphify Action
document.getElementById("btnRunGraphify").addEventListener("click", async () => {
  showToast("Injecting Graphify repository connections...");
  try {
    const data = await postApiRequest("/api/execute", { capability_id: "graphify-injection" });
    showToast("Graphify Injection Completed!");
    console.log("Graphify output:", data);
  } catch (err) {
    console.error(err);
  }
});

// AGENT SANDBOX Action
document.getElementById("btnRunAgentSandbox").addEventListener("click", async () => {
  const agentName = document.getElementById("sandboxAgentSelect").value;
  const prompt = document.getElementById("sandboxAgentPrompt").value.trim();
  
  if (!prompt) {
    showToast("Please enter an instruction prompt for the agent.");
    return;
  }
  
  const statusEl = document.getElementById("sandboxStatus");
  const consoleBody = document.getElementById("sandboxConsoleBody");
  
  statusEl.textContent = "RUNNING";
  statusEl.className = "console-status running";
  
  let accumulatedText = `[SANDBOX START] Initializing agent agentic pipeline for '${agentName}'...\n`;
  consoleBody.innerHTML = linkifyConsoleOutput(accumulatedText);

  try {
    const res = await postApiRequest("/api/agent/run", { agent_name: agentName, prompt: prompt });
    
    // Simulate step-by-step console outputs for premium feel
    let logIndex = 0;
    accumulatedText = "";
    
    function printNextLog() {
      if (logIndex < res.logs.length) {
        accumulatedText += res.logs[logIndex] + "\n";
        consoleBody.innerHTML = linkifyConsoleOutput(accumulatedText);
        logIndex++;
        consoleBody.scrollTop = consoleBody.scrollHeight;
        setTimeout(printNextLog, 650);
      } else {
        accumulatedText += `\n🤖 [AGENT RESPONSE COMPLETED]\n=====================================\n${res.response}`;
        consoleBody.innerHTML = linkifyConsoleOutput(accumulatedText);
        statusEl.textContent = "COMPLETED";
        statusEl.className = "console-status passed";
        consoleBody.scrollTop = consoleBody.scrollHeight;
      }
    }
    
    printNextLog();
    document.getElementById("sandboxAgentPrompt").value = "";
    
  } catch (err) {
    statusEl.textContent = "ERROR";
    statusEl.className = "console-status failed";
    consoleBody.innerHTML = linkifyConsoleOutput(`[AGENT SANDBOX RUNNER FATAL ERROR]\n${err.message}`);
  }
});

// VIEW 7: Course Builder Controller & Catalog Logic
// -------------------------------------------------------------
async function fetchCourses() {
  try {
    const res = await fetch("/api/courses");
    if (!res.ok) throw new Error("API error listing courses");
    const data = await res.json();
    coursesList = data.courses || [];
    renderCourses();
    updateStatsDashboard();
  } catch (err) {
    console.error("Failed to fetch courses:", err);
    document.getElementById("coursesTableBody").innerHTML = `
      <tr>
        <td colspan="7" style="text-align: center; color: var(--text-muted);">
          Course Catalog database offline. Run server.py.
        </td>
      </tr>`;
  }
}

function renderCourses() {
  const tableBody = document.getElementById("coursesTableBody");
  if (!tableBody) return;
  if (coursesList.length === 0) {
    tableBody.innerHTML = `
      <tr>
        <td colspan="7" style="text-align: center; color: var(--text-muted);">
          No generated courses found in directory. Use the builder above to generate one.
        </td>
      </tr>`;
    return;
  }

  tableBody.innerHTML = coursesList.map(c => {
    let statusClass = "console-status";
    if (c.status === "completed") statusClass += " passed";
    else if (c.status === "generating") statusClass += " running";
    else if (c.status === "error") statusClass += " failed";

    const zipAction = c.status === "completed" 
      ? `<a href="#" class="action-btn" style="padding: 4px 8px; font-size: 0.8rem; text-decoration: none; display: inline-block;" onclick="downloadCourseZip(event, '${c.id}')">Download ZIP</a>` 
      : `<span style="color: var(--text-muted);">Processing...</span>`;

    return `
      <tr>
        <td style="font-family: monospace; font-size: 0.85rem;">${c.id}</td>
        <td style="font-weight: 500;">${c.subject}</td>
        <td>${c.audience}</td>
        <td style="text-align: center;">${c.chapters}</td>
        <td><span class="${statusClass}">${c.status.toUpperCase()}</span></td>
        <td>
          <div style="display: flex; align-items: center; gap: 8px;">
            <div style="flex: 1; background: rgba(255,255,255,0.1); height: 6px; border-radius: 3px; min-width: 50px; overflow: hidden;">
              <div style="width: ${c.progress}%; background: var(--accent-gradient); height: 100%;"></div>
            </div>
            <span style="font-size: 0.8rem; font-family: monospace;">${c.progress}%</span>
          </div>
        </td>
        <td>
          <div style="display: flex; gap: 8px; align-items: center;">
            ${zipAction}
            <a href="file://${c.path}/syllabus.md" target="_blank" class="action-btn" style="padding: 4px 8px; font-size: 0.8rem; text-decoration: none; display: inline-block; background: rgba(255,255,255,0.1); border: 1px solid var(--border-glass);">Open Syllabus</a>
          </div>
        </td>
      </tr>
    `;
  }).join("");
}

async function downloadCourseZip(e, courseId) {
  e.preventDefault();
  showToast(`Packaging ${courseId} ZIP archive...`);
  try {
    const res = await postApiRequest("/api/zip", { path: `generated-courses/${courseId}` });
    showToast("ZIP pack ready!");
    
    // Attempt trigger download via standard workspace endpoint or local file link
    const link = document.createElement("a");
    link.href = `/api/zip?path=generated-courses/${courseId}`; // Standard trigger
    showToast(`ZIP saved on local server: ${res.zip_path}`);
  } catch (err) {
    showToast(`Archiving failed: ${err.message}`);
  }
}

// Event handler for blueprint type label updates
const blueprintTypeEl = document.getElementById("blueprintType");
if (blueprintTypeEl) {
  blueprintTypeEl.addEventListener("change", () => {
    const val = blueprintTypeEl.value;
    const lblSubject = document.getElementById("lblSubject");
    const lblAudience = document.getElementById("lblAudience");
    const lblChapters = document.getElementById("lblChapters");
    const lblDescription = document.getElementById("lblDescription");
    const chaptersVal = document.getElementById("courseChapters").value;

    if (val === "course") {
      lblSubject.textContent = "Course Subject / Topic";
      lblAudience.textContent = "Target Audience / Student Level";
      lblChapters.innerHTML = `Number of Chapters / Weeks: <span id="courseChaptersVal">${chaptersVal}</span>`;
      lblDescription.textContent = "Additional Context / Guidelines (Optional)";
    } else if (val === "sop") {
      lblSubject.textContent = "Venture / Business Topic";
      lblAudience.textContent = "Target Sector / Operations Layer";
      lblChapters.innerHTML = `Number of Departments / Modules: <span id="courseChaptersVal">${chaptersVal}</span>`;
      lblDescription.textContent = "Business Context / Specific SOP Focus Areas";
    } else if (val === "prd") {
      lblSubject.textContent = "Product / Feature Title";
      lblAudience.textContent = "Target Platform / Technical Scope";
      lblChapters.innerHTML = `Number of System Modules / Components: <span id="courseChaptersVal">${chaptersVal}</span>`;
      lblDescription.textContent = "Product Requirements Context / API Seed Guidelines";
    }
  });
}

// Event handler for triggering Course Builder
document.getElementById("btnRunCourseBuilder").addEventListener("click", async () => {
  const subject = document.getElementById("courseSubject").value.trim();
  const audience = document.getElementById("courseAudience").value;
  const chapters = document.getElementById("courseChapters").value;
  const narration = document.getElementById("courseNarration").checked;
  const generateImages = document.getElementById("courseImages").checked;
  const description = document.getElementById("courseDescription").value.trim();
  const blueprintType = document.getElementById("blueprintType").value;

  if (!subject) {
    showToast("Please specify a topic first!");
    return;
  }

  const btn = document.getElementById("btnRunCourseBuilder");
  const consoleBody = document.getElementById("courseBuilderConsoleBody");
  const statusEl = document.getElementById("courseBuilderStatus");
  const progressBox = document.getElementById("generationProgressBox");
  const progressBar = document.getElementById("pipelineProgressBar");
  const statusText = document.getElementById("pipelineStatusText");

  btn.disabled = true;
  btn.style.opacity = "0.6";
  progressBox.style.display = "block";
  statusEl.textContent = "RUNNING";
  statusEl.className = "console-status running";
  consoleBody.textContent = `[Knowledge Compiler Start] Initializing blueprint for '${subject}'...\n`;
  progressBar.style.width = "0%";
  statusText.textContent = "Setup";
  
  // Highlight stages
  resetStageHighlights();
  document.getElementById("stage-setup").style.color = "var(--accent-cyan)";
  document.getElementById("stage-setup").style.fontWeight = "bold";

  try {
    const res = await postApiRequest("/api/course/generate", {
      subject, audience, chapters, narration, generateImages, description, blueprintType
    });
    
    activePollingCourseId = res.course_id;
    showToast("Course generation pipeline triggered!");
    
    // Start polling progress logs
    if (pollingIntervalId) clearInterval(pollingIntervalId);
    pollingIntervalId = setInterval(pollCourseProgress, 1000);

  } catch (err) {
    btn.disabled = false;
    btn.style.opacity = "1";
    statusEl.textContent = "ERROR";
    statusEl.className = "console-status failed";
    consoleBody.textContent = `[CURRICULUM ENGINE FATAL ERROR]\n${err.message}`;
  }
});

function resetStageHighlights() {
  ["stage-setup", "stage-syllabus", "stage-research", "stage-build", "stage-export"].forEach(id => {
    const el = document.getElementById(id);
    if (el) {
      el.style.color = "var(--text-muted)";
      el.style.fontWeight = "normal";
    }
  });
}

async function pollCourseProgress() {
  if (!activePollingCourseId) return;
  try {
    const res = await fetch(`/api/course/status?id=${activePollingCourseId}`);
    if (!res.ok) throw new Error("Status query failed");
    const data = await res.json();

    const consoleBody = document.getElementById("courseBuilderConsoleBody");
    const statusEl = document.getElementById("courseBuilderStatus");
    const progressBar = document.getElementById("pipelineProgressBar");
    const statusText = document.getElementById("pipelineStatusText");

    // Print logs
    consoleBody.textContent = data.logs.join("\n") + "\n";
    consoleBody.scrollTop = consoleBody.scrollHeight;

    // Update progress bar
    progressBar.style.width = `${data.progress}%`;

    // Highlight active stages based on progress percentage
    resetStageHighlights();
    if (data.progress < 25) {
      statusText.textContent = "Setup Stage";
      document.getElementById("stage-setup").style.color = "var(--accent-cyan)";
      document.getElementById("stage-setup").style.fontWeight = "bold";
    } else if (data.progress < 50) {
      statusText.textContent = "Syllabus Stage";
      document.getElementById("stage-syllabus").style.color = "var(--accent-cyan)";
      document.getElementById("stage-syllabus").style.fontWeight = "bold";
    } else if (data.progress < 60) {
      statusText.textContent = "Research Stage";
      document.getElementById("stage-research").style.color = "var(--accent-cyan)";
      document.getElementById("stage-research").style.fontWeight = "bold";
    } else if (data.progress < 95) {
      statusText.textContent = `Build Stage (Chapter Artifacts)`;
      document.getElementById("stage-build").style.color = "var(--accent-cyan)";
      document.getElementById("stage-build").style.fontWeight = "bold";
    } else {
      statusText.textContent = "Exporting / Packaging";
      document.getElementById("stage-export").style.color = "var(--accent-cyan)";
      document.getElementById("stage-export").style.fontWeight = "bold";
    }

    if (data.status === "completed" || data.status === "error") {
      clearInterval(pollingIntervalId);
      pollingIntervalId = null;
      activePollingCourseId = null;

      const btn = document.getElementById("btnRunCourseBuilder");
      btn.disabled = false;
      btn.style.opacity = "1";

      if (data.status === "completed") {
        statusEl.textContent = "COMPLETED";
        statusEl.className = "console-status passed";
        showToast("Course generation completed successfully!");
      } else {
        statusEl.textContent = "ERROR";
        statusEl.className = "console-status failed";
        showToast("Course generation failed!");
      }
      
      // Refresh course list catalog
      fetchCourses();
      
      // Clear inputs
      document.getElementById("courseSubject").value = "";
      document.getElementById("courseDescription").value = "";
    }

  } catch (err) {
    console.error("Polling error:", err);
  }
}

// Linkify utility for ports, localhost URLs, and custom URLs in console outputs
function linkifyConsoleOutput(text) {
  // 1. Escape HTML first
  let escaped = text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");

  // 2. Linkify standard http://localhost:XXXX URLs
  escaped = escaped.replace(/(https?:\/\/localhost:(\d+)[^\s]*)/gi, (url) => {
    return `<a href="${url}" target="_blank" class="console-link" style="color: var(--primary-accent, #6366f1); text-decoration: underline; font-weight: 600;">${url}</a>`;
  });

  // 3. Linkify "localhost:XXXX"
  escaped = escaped.replace(/(?<!https?:\/\/)(localhost:(\d+))/gi, (match, p1, p2) => {
    return `<a href="http://localhost:${p2}" target="_blank" class="console-link" style="color: var(--primary-accent, #6366f1); text-decoration: underline; font-weight: 600;">${match}</a>`;
  });

  // 4. Linkify "Port XXXX" or "port XXXX"
  escaped = escaped.replace(/(ports?\s+(\d+))/gi, (match, p1, p2) => {
    return `${p1.split(/\s+/)[0]} <a href="http://localhost:${p2}" target="_blank" class="console-link" style="color: var(--primary-accent, #6366f1); text-decoration: underline; font-weight: 600;">${p2}</a>`;
  });

  return escaped;
}

// -------------------------------------------------------------
// VIEW 8: AIP Control Plane Logic
// -------------------------------------------------------------
async function fetchFrameworks() {
  try {
    const res = await fetch("/api/registry/frameworks");
    if (!res.ok) throw new Error("API error fetching frameworks");
    const jsonRes = await res.json();
    registryFrameworks = jsonRes.data || [];
    renderFrameworks();
    updateStatsDashboard();
  } catch (err) {
    console.error(err);
    document.getElementById("frameworksTableBody").innerHTML = `
      <tr>
        <td colspan="6" style="text-align: center; color: var(--text-muted); padding: 20px;">Frameworks Registry Unavailable</td>
      </tr>`;
  }
}

function renderFrameworks() {
  const tbody = document.getElementById("frameworksTableBody");
  if (!tbody || registryFrameworks.length === 0) return;

  const list = registryFrameworks.filter(f => f.id);

  tbody.innerHTML = list.map(f => `
    <tr>
      <td style="font-weight: 600; color: var(--text-primary);">${f.name}</td>
      <td style="color: var(--text-secondary);">${f.orchestration}</td>
      <td style="font-family: monospace; color: var(--accent-cyan);">${f.language}</td>
      <td style="color: ${f.mcp_support === "true" || f.mcp_support === true ? "var(--accent-cyan)" : "var(--text-muted)"}">${f.mcp_support === "true" || f.mcp_support === true ? "✅ Active" : "❌ No"}</td>
      <td style="font-weight: 500; color: var(--text-primary);">${f.scalability}</td>
      <td style="font-weight: 600; color: var(--accent-pink);">${f.enterprise_readiness}</td>
    </tr>
  `).join("");
}

async function fetchModels() {
  try {
    const res = await fetch("/api/registry/models");
    if (!res.ok) throw new Error("API error fetching models");
    const jsonRes = await res.json();
    registryModels = jsonRes.data || [];
    renderModels();
    updateStatsDashboard();
  } catch (err) {
    console.error(err);
    document.getElementById("modelsTableBody").innerHTML = `
      <tr>
        <td colspan="7" style="text-align: center; color: var(--text-muted); padding: 20px;">Models Registry Unavailable</td>
      </tr>`;
  }
}

function renderModels() {
  const tbody = document.getElementById("modelsTableBody");
  if (!tbody || registryModels.length === 0) return;

  const list = registryModels.filter(m => m.id);

  tbody.innerHTML = list.map(m => `
    <tr>
      <td style="font-weight: 600; color: var(--text-primary);">${m.name}</td>
      <td style="font-weight: 500; color: var(--accent-cyan);">${m.provider}</td>
      <td style="font-weight: 600; color: var(--accent-green);">${m.quality_score}</td>
      <td style="font-weight: 600; color: var(--accent-pink);">${m.coding_score}</td>
      <td style="font-family: monospace; color: var(--text-secondary);">${m.latency_ms} ms</td>
      <td style="font-family: monospace; color: var(--text-primary);">$${parseFloat(m.cost_input_1m).toFixed(2)} / $${parseFloat(m.cost_output_1m).toFixed(2)}</td>
      <td style="color: ${m.reasoning_budget === "true" || m.reasoning_budget === true ? "var(--accent-cyan)" : "var(--text-muted)"}">${m.reasoning_budget === "true" || m.reasoning_budget === true ? "⚡ Enabled" : "❌ No"}</td>
    </tr>
  `).join("");
}

// App Initialization
function init() {
  initTheme();
  
  // Set stat values on load
  totalCountEl.textContent = resourcesData.length;
  categoryCountEl.textContent = Object.keys(categoryStyles).length;
  updateBookmarkStats();
  
  renderCategoryTabs();
  renderCards(resourcesData);

  // Prefetch operational catalogs asynchronously on load
  fetchCapabilities();
  fetchRepositories();
  fetchAgents();
  fetchGraphData();
  fetchCourses();
  fetchFrameworks();
  fetchModels();
}

document.addEventListener("DOMContentLoaded", init);
