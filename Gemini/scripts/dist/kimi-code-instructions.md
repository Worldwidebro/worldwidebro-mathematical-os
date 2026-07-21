# AI-BOSS-OS Workspace Instructions & Capabilities Registry

This file defines the system architecture, model policies, and available agent blueprints for this workspace.

## 1. System Map & Core Ports
- **OmniRoute Gateway**: `http://localhost:20128/v1`
- **Ollama**: Port `11434` (models mapped from external storage)
- **Neo4j Graph Database**: Ports `7474` (HTTP) / `7687` (Bolt)
- **Qdrant Vector DB**: Port `6333` (Docker container: `civos_qdrant`)
- **Langfuse Tracing Dashboard**: Port `3003` (Docker container: `civos_langfuse`)

## 2. Model Routing Table (`auto/*`)
| Logical Tag | Primary Target | Fallback Target | Description |
| :--- | :--- | :--- | :--- |
| `auto` | anthropic/claude-3-5-sonnet | openai/gpt-4o | Centralized route tag |
| `auto/coding` | anthropic/claude-3-5-sonnet | deepseek/deepseek-coder | Centralized route tag |
| `auto/smart` | anthropic/claude-3-5-sonnet | openai/gpt-4o | Centralized route tag |
| `auto/cheap` | deepseek/deepseek-chat | openai/gpt-4o-mini | Centralized route tag |
| `auto/fast` | openai/gpt-4o-mini | anthropic/claude-3-5-haiku | Centralized route tag |
| `auto/offline` | ollama/qwen2.5-coder-32b | ollama/llama3-8b | Centralized route tag |

## 3. Registered Agents
### CTO
- **Default Routing Model**: `{}`
- **Tools**: `github, filesystem`
- **Escalation Target**: `{}`

### CFO
- **Default Routing Model**: `{}`
- **Tools**: `database, calculator`
- **Escalation Target**: `{}`

### Research
- **Default Routing Model**: `{}`
- **Tools**: `web-search, read-url`
- **Escalation Target**: `{}`

## 4. LLM Councils (Governance)
### Acquisition Council
- **Members**: claude, gpt, gemini
- **Chairman**: `{}`
- **Consensus Threshold**: `{}`

## 5. Agent Blueprints Catalog
### Custom Enterprise Agents
| Agent Name | Industry | Role / Description | Source |
| :--- | :--- | :--- | :--- |
| HIA (Health Insights Agent) | Healthcare | Analyses medical reports and provides health insights | GitHub |
| AI Health Assistant | Healthcare | Diagnoses and monitors diseases using patient data | GitHub |
| Automated Trading Bot | Finance | Automates stock trading with real-time market analysis | GitHub |
| Agent Wallet SDK | Finance | Non-custodial smart contract wallet SDK for AI agents with enforced spend limits | GitHub |
| Virtual AI Tutor | Education | Provides personalized education tailored to users | GitHub |
| 24/7 AI Chatbot | Customer Service | Handles customer queries around the clock | GitHub |
| Product Recommendation Agent | Retail | Suggests products based on user preferences and history | GitHub |
| Self-Driving Delivery Agent | Transportation | Optimizes routes and autonomously delivers packages | GitHub |
| Factory Process Monitoring Agent | Manufacturing | Monitors production lines and ensures quality control | GitHub |
| Property Pricing Agent | Real Estate | Analyzes market trends to determine property prices | GitHub |
| Smart Farming Assistant | Agriculture | Provides insights on crop health and yield predictions | GitHub |
| Energy Demand Forecasting Agent | Energy | Predicts energy usage to optimize grid management | GitHub |
| Content Personalization Agent | Entertainment | Recommends personalized media based on preferences | GitHub |
| Legal Document Review Assistant | Legal | Automates document review and highlights key clauses | GitHub |
| Recruitment Recommendation Agent | Human Resources | Suggests best-fit candidates for job openings | GitHub |
| Virtual Travel Assistant | Hospitality | Plans travel itineraries based on preferences | GitHub |
| AI Game Companion Agent | Gaming | Enhances player experience with real-time assistance | GitHub |
| Real-Time Threat Detection Agent | Cybersecurity | Identifies potential threats and mitigates attacks | GitHub |
| E-commerce Personal Shopper Agent | E-commerce | Helps customers find products they'll love | GitHub |
| Logistics Optimization Agent | None | Plans efficient delivery routes and manages inventory | GitHub |
| Vibe Hacking Agent | Cybersecurity | Autonomous Multi-Agent Based Red Team Testing Service | GitHub |
| Citadel | Software Development | Orchestrates Claude Code agent fleets with lifecycle hooks, skills, campaign management, and postmortem-driven architecture | GitHub |
| MediSuite-AI-Agent | Health Insurance | Automates hospital / insurance claiming workflow | GitHub |
| Lina Egyptian Medical Chatbot | Healthcare | Egyptian medical assistant chatbot | GitHub |

### CrewAI Framework Blueprints
| Use Case | Industry | Description | Source |
| :--- | :--- | :--- | :--- |
| Email Auto Responder Flow | Communication | Automates email responses based on predefined criteria | GitHub |
| Meeting Assistant Flow | Productivity | Organizes meetings, scheduling and agenda preparation | GitHub |
| Self Evaluation Loop Flow | Human Resources | Facilitates self-assessment for performance reviews | GitHub |
| Lead Score Flow | Sales | Evaluates and scores potential leads to prioritize outreach | GitHub |
| Marketing Strategy Generator | Marketing | Develops marketing strategies by analyzing market trends | GitHub |
| Job Posting Generator | Recruitment | Creates job postings by analyzing job requirements | GitHub |
| Recruitment Workflow | Recruitment | Streamlines recruitment by automating hiring tasks | GitHub |
| Match Profile to Positions | Recruitment | Matches candidate profiles to suitable job positions | GitHub |
| Instagram Post Generator | Social Media | Generates and schedules Instagram posts automatically | GitHub |
| Landing Page Generator | Web Development | Automates creation of landing pages for websites | GitHub |
| Game Builder Crew | Game Development | Assists in game development by automating aspects of creation | GitHub |
| Stock Analysis Tool | Finance | Provides tools for analyzing stock market data | GitHub |
| Trip Planner | Travel | Assists in planning trips with itineraries | GitHub |
| Surprise Trip Planner | Travel | Plans surprise trips based on user preferences | GitHub |
| Write a Book with Flows | Creative Writing | Assists authors with structured writing workflows | GitHub |
| Screenplay Writer | Creative Writing | Aids in writing screenplays with templates and guidance | GitHub |
| Markdown Validator | Documentation | Validates Markdown files for proper formatting | GitHub |
| Meta Quest Knowledge | Knowledge Management | Manages Meta Quest knowledge for information retrieval | GitHub |
| NVIDIA Models Integration | AI Integration | Integrates NVIDIA AI models into workflows | GitHub |
| Prep for a Meeting | Productivity | Prepares meeting materials and sets agendas | GitHub |
| Starter Template | Development | Starter template for new CrewAI projects | GitHub |
| CrewAI + LangGraph Integration | AI Integration | Integration between CrewAI and LangGraph | GitHub |

### AutoGen Multi-Agent Collaboration Blueprints
| Use Case | Industry | Description | Source |
| :--- | :--- | :--- | :--- |
| Automated Task Solving with Code Gen, Execution & Debugging | Software Development | Demonstrates automated task-solving by generating, executing, and debugging code | Notebook |
| Code Generation and Q&A with Retrieval Augmented Agents | Software Development | Generates code and answers questions using retrieval-augmented methods | Notebook |
| Code Generation and Q&A with Qdrant-based Retrieval | Software Development | Utilizes Qdrant for enhanced retrieval-augmented agent performance | Notebook |
| Group Chat (3 members, 1 manager) | Collaboration | Demonstrates group task-solving via multi-agent collaboration | Notebook |
| Data Visualization by Group Chat | Data Analysis | Uses multi-agent collaboration to create data visualizations | Notebook |
| Complex Task Solving by Group Chat (6 members) | Collaboration | Solves complex tasks collaboratively with a larger group | Notebook |
| Task Solving with Coding & Planning Agents | Planning & Dev | Combines coding and planning agents for solving tasks | Notebook |
| Task Solving with Graph Transition Paths | Collaboration | Uses predefined transition paths in a graph for solving tasks | Notebook |
| SocietyOfMindAgent Inner-Monologue | Cognitive Sciences | Simulates inner-monologue for problem-solving using group chats | Notebook |
| Group Chat with Custom Speaker Selection | Collaboration | Implements a custom function for speaker selection | Notebook |
| Sequential Task-Solving (single initiating agent) | Workflow Automation | Automates sequential task-solving with a single initiating agent | Notebook |
| Async Sequential Task-Solving | Workflow Automation | Handles asynchronous task-solving in a sequence of chats | Notebook |
| Sequential Chats with Different Initiating Agents | Workflow Automation | Sequential task-solving with different agents initiating each chat | Notebook |
| Solving Complex Tasks with Nested Chats | Problem Solving | Uses nested chats to solve hierarchical and complex problems | Notebook |
| Sequence of Nested Chats | Problem Solving | Demonstrates sequential task-solving using nested chats | Notebook |
| OptiGuide Supply Chain with Nested Chats | Supply Chain | Solves supply chain optimization using nested chats | Notebook |
| Conversational Chess with Nested Chats | Gaming | Uses nested chats for playing conversational chess with tools | Notebook |
| Web Search: Solve Tasks Requiring Web Info | Information Retrieval | Searches the web to gather information for completing tasks | Notebook |
| Use Provided Tools as Functions | Tool Integration | Demonstrates how to use pre-provided tools as callable functions | Notebook |
| RAG Group Chat | Collaboration | Enables group chat with Retrieval Augmented Generation | Notebook |
| Agent Chat with Whisper | Audio Processing | AI agent for transcription and translation using Whisper | Notebook |
| SQL: Natural Language to SQL Query | Database Management | Converts natural language inputs into SQL queries | Notebook |
| Multimodal Agent with DALLE and GPT-4V | Multimedia AI | Combines DALLE and GPT-4V for multimodal agent communication | Notebook |
| Multimodal Agent with Llava | Image Processing | Uses Llava for multimodal agent conversations | Notebook |
| Multimodal Agent with GPT-4V | Multimedia AI | Leverages GPT-4V for visual and conversational interactions | Notebook |
| AgentEval: Multi-Agent Assessment System | Performance Evaluation | Evaluating LLM-based application utility | Notebook |
| Track LLM Calls and Errors using AgentOps | Monitoring & Analytics | Monitors LLM interactions, tool usage, and errors | Notebook |
| Auto Build Multi-agent System with AgentBuilder | AI Development | Automatically builds multi-agent systems | Notebook |

### Agno Lightweight Blueprints
| Agent Name | Industry | Description | Language |
| :--- | :--- | :--- | :--- |
| Support Agent | AI Framework Support | Real-time answers, explanations, and code examples for Agno framework | Python |
| YouTube Agent | Media & Content | Analyzes YouTube videos: summaries, timestamps, themes | Python |
| Finance Agent (Thinking) | Finance | Real-time stock insights, analyst recommendations, financial deep-dives | Python |
| Study Partner | Education | Finds resources, answers questions, creates study plans | Python |
| Shopping Partner Agent | E-commerce | Product recommender based on preferences from Amazon, Flipkart | Python |
| Research Scholar Agent | Education / Research | Advanced academic searches, publication analysis, structured reports | Python |
| Research Agent | Media & Journalism | Deep investigations, NYT-style reports | Python |
| Recipe Creator | Food & Culinary | Personalized recipes based on ingredients and preferences | Python |
| Financial Reasoning Agent | Finance | Claude 3.5 Sonnet-based stock analysis with Yahoo Finance data | Python |
| Readme Generator Agent | Software Dev | Generates high-quality READMEs for GitHub repos | Python |
| Movie Recommendation Agent | Entertainment | Personalized movie recommendations using Exa and GPT-4o | Python |
| Media Trend Analysis Agent | Media & News | Analyzes emerging trends and influencers from digital platforms | Python |
| Legal Document Analysis Agent | Legal Tech | Analyzes legal PDFs and provides insights using vector embeddings | Python |
| DeepKnowledge | Research | Iterative search through knowledge base with deep reasoning | Python |
| Book Recommendation Agent | Publishing & Media | Personalized book suggestions using literary data and reader preferences | Python |
| MCP Airbnb Agent | Hospitality | Search Airbnb listings with MCP and Llama 4 | Python |
| Agno Assist Agent | AI Framework | GPT-4o agent for Agno framework Q&A with hybrid search | Python |

### LangGraph State-Machine Workflows
| Use Case | Industry | Description | Language |
| :--- | :--- | :--- | :--- |
| Chatbot Simulation Evaluation | AI / QA | Simulate user interactions to evaluate chatbot performance | Python |
| Information Gathering via Prompting | Research | LangGraph workflow using prompting to gather information | Python |
| Code Assistant with LangGraph | Software Development | Resilient code assistant with error checking and iterative refinement | Python |
| Customer Support Agent | Customer Support | Graph-based agent for handling customer inquiries | Python |
| Extraction with Retries | Data Extraction | Retry mechanisms for robust data extraction | Python |
| Multi-Agent Workflow (Supervisor) | Workflow Orchestration | Supervisor agent orchestrating multiple specialized agents | Python |
| Hierarchical Agent Teams | Workflow Orchestration | Top-level supervisor delegates to specialized sub-agents | Python |
| Multi-Agent Collaboration | Workflow Orchestration | Multiple specialized agents working together on complex tasks | Python |
| Plan-and-Execute Agent | Workflow Orchestration | Agent generates multi-step plan then executes sequentially | Python |
| SQL Agent | Database Interaction | Agent answers questions about SQL databases | Python |
| Reflection Agent | Workflow Orchestration | Agent critiques and revises its own outputs | Python |
| Reflexion Agent | Workflow Orchestration | Agent reflects on actions for iterative improvement | Python |
| Adaptive RAG | Information Retrieval | Dynamic retrieval adjusting based on query complexity | Python |
| Agentic RAG | Intelligent Agents | Agent determines best retrieval strategy before generating response | Python |
| Corrective RAG (CRAG) | Information Retrieval | Evaluates and refines retrieved documents before generation | Python |
| Self-RAG | Information Retrieval | System reflects on responses and retrieves additional info if needed | Python |
| Adaptive RAG (Local) | Information Retrieval | Adaptive RAG with local models for offline use | Python |
| Self-RAG (Local) | Information Retrieval | Self-RAG using local models and data sources | Python |
