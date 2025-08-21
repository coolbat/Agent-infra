# Agent Infra

🚀 A curated list of **Agent Infrastructure (Agent Infra)** resources, frameworks, tools, and tutorials.  
The goal is to help developers understand, build, and explore the ecosystem around **AI Agents**.

---

## 📖 Table of Contents
- [Introduction](#-introduction)
- [Core Components](#-core-components)
  - [Runtime / Sandbox](#runtime--sandbox)
  - [Memory & State](#memory--state)
  - [Orchestration & Workflow](#orchestration--workflow)
  - [Communication Protocols](#communication-protocols)
  - [Tools & Plugins](#tools--plugins)
  - [Security & Governance](#security--governance)
  - [Observability & Monitoring](#observability--monitoring)
- [Frameworks](#-frameworks)
- [Developer Tools (DX)](#-developer-tools-dx)
- [Privacy & Local-first](#-privacy--local-first)
- [Learning Resources](#-learning-resources)
- [Demos & Examples](#-demos--examples)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌐 Introduction
**Agent Infra** refers to the underlying infrastructure that powers **AI Agents**.  
It includes runtime environments, memory, orchestration, communication protocols, tool/plugin systems, security, monitoring, and developer experience.

This repository collects awesome projects and resources to explore the **Agent Infra ecosystem**.

---

## ⚙️ Core Components

### Runtime / Sandbox
- [Semantic Kernel Runtime](https://github.com/microsoft/semantic-kernel) – Lightweight runtime for AI agents.  
- [WebLLM](https://github.com/mlc-ai/web-llm) – LLM inference in the browser with WebGPU.  

### Memory & State
- [LlamaIndex](https://github.com/jerryjliu/llama_index) – Data framework for LLM applications.  
- [Chroma](https://www.trychroma.com/) – Open-source embedding database.  
- [Weaviate](https://weaviate.io/) – Vector database for contextual memory.  

### Orchestration & Workflow
- [LangGraph](https://github.com/langchain-ai/langgraph) – Graph-based orchestration for agents.  
- [AutoGen](https://github.com/microsoft/autogen) – Multi-agent conversation orchestration.  
- [CrewAI](https://github.com/joaomdmoura/crewai) – Framework for multi-agent workflows.  

### Communication Protocols
- [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) – Open protocol for LLM ↔ tools.  
- [LangServe](https://github.com/langchain-ai/langserve) – Deploy LangChain apps as APIs.  

### Tools & Plugins
- [OpenAI MCP Tools](https://github.com/modelcontextprotocol) – Official MCP plugin examples.  
- [Notion Agent Plugin](#) – Example integration with Notion.  

### Security & Governance
- [Guardrails AI](https://github.com/ShreyaR/guardrails) – Validating and enforcing LLM outputs.  
- [Rebuff](https://github.com/protectai/rebuff) – Prompt injection detection.  

### Observability & Monitoring
- [Langfuse](https://github.com/langfuse/langfuse) – Open-source observability for LLM apps.  
- [Helicone](https://github.com/Helicone/helicone) – Logging & monitoring for LLM APIs.  
- [PromptLayer](https://www.promptlayer.com/) – Prompt tracking and management.  

---

## 🏗 Frameworks
- [LangChain](https://github.com/langchain-ai/langchain) – End-to-end agentic app framework.  
- [Semantic Kernel](https://github.com/microsoft/semantic-kernel) – AI orchestration by Microsoft.  
- [Haystack Agents](https://haystack.deepset.ai/) – Agent framework for enterprise.  
- [ChatDev](https://github.com/OpenBMB/ChatDev) – Multi-agent software development simulation.  

---

## 🛠 Developer Tools (DX)
- [Chainlit](https://github.com/Chainlit/chainlit) – UI for developing LLM apps.  
- [Gradio](https://github.com/gradio-app/gradio) – Build & share ML/LLM UIs.  
- [Promptfoo](https://github.com/promptfoo/promptfoo) – Test and evaluate prompts.  

---

## 🔒 Privacy & Local-first
- [Ollama](https://github.com/ollama/ollama) – Run LLMs locally with a simple CLI.  
- [PrivateGPT](https://github.com/imartinez/privateGPT) – Ask questions about documents locally.  
- [Llama.cpp](https://github.com/ggerganov/llama.cpp) – Inference of LLaMA models on CPU.  

---

## 📚 Learning Resources
- [Agent Infra 101 Blog](#) – Intro to AI Agent Infrastructure.  
- [Multi-Agent Systems Survey](#) – Research papers and surveys.  
- [MCP Introduction](https://modelcontextprotocol.io/) – Learn about Model Context Protocol.  

---

## 🎮 Demos & Examples
- [AI Town](https://github.com/a16z-infra/ai-town) – Multi-agent social simulation.  
- [BabyAGI](https://github.com/yoheinakajima/babyagi) – Autonomous task management agent.  
- [Superagent](https://github.com/homanp/superagent) – Open-source AI assistant.  

---

Below are resources automatically updated by our script.  
You can add your own curated items **outside this block**, they will not be overwritten.

<!-- AGENT-INFRA-START -->
### Framework
- [lobe-chat](https://github.com/lobehub/lobe-chat) ⭐64690
  - 🤯 Lobe Chat - an open-source, modern design AI chat framework. Supports multiple AI providers (OpenAI / Claude 4 / Gemini / DeepSeek / Ollama / Qwen), Knowledge Base (file upload / RAG ), one click install MCP Marketplace and Artifacts / Thinking. One-click FREE deployment of your private AI Agent application.
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) ⭐57997
  - 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming
- [crewAI](https://github.com/crewAIInc/crewAI) ⭐35946
  - Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.
- [agno](https://github.com/agno-agi/agno) ⭐32042
  - Open-source framework for building multi-agent systems with memory, knowledge and reasoning.
- [haystack](https://github.com/deepset-ai/haystack) ⭐21958
  - AI orchestration framework to build customizable, production-ready LLM applications. Connect components (models, vector DBs, file converters) to pipelines or agents that can interact with your data. With advanced retrieval methods, it's best suited for building RAG, question answering, semantic search or conversational agent chatbots.
- [letta](https://github.com/letta-ai/letta) ⭐17983
  - Letta (formerly MemGPT) is the stateful agents framework with memory, reasoning, and context management.
- [DB-GPT](https://github.com/eosphoros-ai/DB-GPT) ⭐17183
  - AI Native Data App Development framework with AWEL(Agentic Workflow Expression Language) and Agents
- [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) ⭐16647
  - <⚡️> SuperAGI - A dev-first open source autonomous AI agent framework. Enabling developers to build, manage & run useful autonomous agents quickly and reliably.
- [RagaAI-Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) ⭐16051
  - Python SDK for Agent AI Observability, Monitoring and Evaluation Framework. Includes features like agent, llm and tools tracing, debugging multi-agentic system, self-hosted dashboard and advanced analytics with timeline and execution graph view 
- [PraisonAI](https://github.com/MervinPraison/PraisonAI) ⭐5297
  - PraisonAI is a production-ready Multi AI Agents framework, designed to create AI Agents to automate and solve problems ranging from simple tasks to complex challenges. It provides a low-code solution to streamline the building and management of multi-agent LLM systems, emphasising simplicity, customisation, and effective human-agent collaboration.
- [DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent) ⭐1400
  - DeepResearchAgent is a hierarchical multi-agent system designed not only for deep research tasks but also for general-purpose task solving. The framework leverages a top-level planning agent to coordinate multiple specialized lower-level agents, enabling automated task decomposition and efficient execution across diverse and complex domains.
- [KaibanJS](https://github.com/kaiban-ai/KaibanJS) ⭐1232
  - KaibanJS is a JavaScript-native framework for building and managing multi-agent systems  with a Kanban-inspired approach.
- [Agent-MCP](https://github.com/rinadelph/Agent-MCP) ⭐830
  - Agent-MCP is a framework for creating multi-agent systems that enables coordinated, efficient AI collaboration through the Model Context Protocol (MCP). The system is designed for developers building AI applications that benefit from multiple specialized agents working in parallel on different aspects of a project.
- [Sage](https://github.com/ZHangZHengEric/Sage) ⭐574
  - Multi-Agent System Framework For Complex Tasks
- [agent-zero](https://github.com/agent0ai/agent-zero) ⭐11556
  - Agent Zero AI framework
- [txtai](https://github.com/neuml/txtai) ⭐11443
  - 💡 All-in-one open-source AI framework for semantic search, LLM orchestration and language model workflows
- [higgsfield](https://github.com/higgsfield-ai/higgsfield) ⭐3459
  - Fault-tolerant, highly scalable GPU orchestration, and a machine learning framework designed for training models with billions to trillions of parameters

### Memory
- [agno](https://github.com/agno-agi/agno) ⭐32042
  - Open-source framework for building multi-agent systems with memory, knowledge and reasoning.
- [haystack](https://github.com/deepset-ai/haystack) ⭐21958
  - AI orchestration framework to build customizable, production-ready LLM applications. Connect components (models, vector DBs, file converters) to pipelines or agents that can interact with your data. With advanced retrieval methods, it's best suited for building RAG, question answering, semantic search or conversational agent chatbots.
- [letta](https://github.com/letta-ai/letta) ⭐17983
  - Letta (formerly MemGPT) is the stateful agents framework with memory, reasoning, and context management.
- [FastGPT](https://github.com/labring/FastGPT) ⭐25560
  - FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.
- [Show HN: I replaced vector databases with Git for AI memory (PoC)](https://github.com/Growth-Kinetics/DiffMem)
  - <a href="https://news.ycombinator.com/item?id=44969622">Comments</a>

### Orchestration
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) ⭐57997
  - 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming
- [agno](https://github.com/agno-agi/agno) ⭐32042
  - Open-source framework for building multi-agent systems with memory, knowledge and reasoning.
- [haystack](https://github.com/deepset-ai/haystack) ⭐21958
  - AI orchestration framework to build customizable, production-ready LLM applications. Connect components (models, vector DBs, file converters) to pipelines or agents that can interact with your data. With advanced retrieval methods, it's best suited for building RAG, question answering, semantic search or conversational agent chatbots.
- [DB-GPT](https://github.com/eosphoros-ai/DB-GPT) ⭐17183
  - AI Native Data App Development framework with AWEL(Agentic Workflow Expression Language) and Agents
- [RagaAI-Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) ⭐16051
  - Python SDK for Agent AI Observability, Monitoring and Evaluation Framework. Includes features like agent, llm and tools tracing, debugging multi-agentic system, self-hosted dashboard and advanced analytics with timeline and execution graph view 
- [PraisonAI](https://github.com/MervinPraison/PraisonAI) ⭐5297
  - PraisonAI is a production-ready Multi AI Agents framework, designed to create AI Agents to automate and solve problems ranging from simple tasks to complex challenges. It provides a low-code solution to streamline the building and management of multi-agent LLM systems, emphasising simplicity, customisation, and effective human-agent collaboration.
- [DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent) ⭐1400
  - DeepResearchAgent is a hierarchical multi-agent system designed not only for deep research tasks but also for general-purpose task solving. The framework leverages a top-level planning agent to coordinate multiple specialized lower-level agents, enabling automated task decomposition and efficient execution across diverse and complex domains.
- [KaibanJS](https://github.com/kaiban-ai/KaibanJS) ⭐1232
  - KaibanJS is a JavaScript-native framework for building and managing multi-agent systems  with a Kanban-inspired approach.
- [Agent-MCP](https://github.com/rinadelph/Agent-MCP) ⭐830
  - Agent-MCP is a framework for creating multi-agent systems that enables coordinated, efficient AI collaboration through the Model Context Protocol (MCP). The system is designed for developers building AI applications that benefit from multiple specialized agents working in parallel on different aspects of a project.
- [ai-doc-gen](https://github.com/divar-ir/ai-doc-gen) ⭐593
  - AI-powered multi-agent system that automatically analyzes codebases and generates comprehensive documentation. Features GitLab integration, concurrent processing, and multiple LLM support for better code understanding and developer onboarding.
- [Sage](https://github.com/ZHangZHengEric/Sage) ⭐574
  - Multi-Agent System Framework For Complex Tasks
- [swe-agent](https://github.com/langtalks/swe-agent) ⭐524
  - 🤖 AI-powered software engineering multi-agent system with researcher and developer agents that automate code implementation through intelligent planning and execution. Built with LangGraph multi-agent workflows
- [dify](https://github.com/langgenius/dify) ⭐111636
  - Production-ready platform for agentic workflow development.
- [FastGPT](https://github.com/labring/FastGPT) ⭐25560
  - FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities such as data processing, RAG retrieval, and visual AI workflow orchestration, letting you easily develop and deploy complex question-answering systems without the need for extensive setup or configuration.
- [txtai](https://github.com/neuml/txtai) ⭐11443
  - 💡 All-in-one open-source AI framework for semantic search, LLM orchestration and language model workflows
- [bisheng](https://github.com/dataelement/bisheng) ⭐9486
  - BISHENG is an open LLM devops platform for next generation Enterprise AI applications. Powerful and comprehensive features include: GenAI workflow, RAG, Agent, Unified model management, Evaluation, SFT, Dataset Management, Enterprise-level System Management, Observability and more.
- [flyte](https://github.com/flyteorg/flyte) ⭐6426
  - Scalable and flexible workflow orchestration platform that seamlessly unifies data, ML and analytics stacks.
- [poml](https://github.com/microsoft/poml) ⭐3640
  - Prompt Orchestration Markup Language
- [higgsfield](https://github.com/higgsfield-ai/higgsfield) ⭐3459
  - Fault-tolerant, highly scalable GPU orchestration, and a machine learning framework designed for training models with billions to trillions of parameters

### Plugins
- [RagaAI-Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) ⭐16051
  - Python SDK for Agent AI Observability, Monitoring and Evaluation Framework. Includes features like agent, llm and tools tracing, debugging multi-agentic system, self-hosted dashboard and advanced analytics with timeline and execution graph view 
- [DevOpsGPT](https://github.com/kuafuai/DevOpsGPT) ⭐5960
  - Multi agent system for AI-driven software development. Combine LLM with DevOps tools to convert natural language requirements into working software. Supports any development language and extends the existing code.
- [ai-doc-gen](https://github.com/divar-ir/ai-doc-gen) ⭐593
  - AI-powered multi-agent system that automatically analyzes codebases and generates comprehensive documentation. Features GitLab integration, concurrent processing, and multiple LLM support for better code understanding and developer onboarding.
- [MCP for Research: How to Connect AI to Research Tools](https://huggingface.co/blog/mcp-for-research)
  - No description

### Runtime
- [RagaAI-Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) ⭐16051
  - Python SDK for Agent AI Observability, Monitoring and Evaluation Framework. Includes features like agent, llm and tools tracing, debugging multi-agentic system, self-hosted dashboard and advanced analytics with timeline and execution graph view 
- [DeepResearchAgent](https://github.com/SkyworkAI/DeepResearchAgent) ⭐1400
  - DeepResearchAgent is a hierarchical multi-agent system designed not only for deep research tasks but also for general-purpose task solving. The framework leverages a top-level planning agent to coordinate multiple specialized lower-level agents, enabling automated task decomposition and efficient execution across diverse and complex domains.
- [swe-agent](https://github.com/langtalks/swe-agent) ⭐524
  - 🤖 AI-powered software engineering multi-agent system with researcher and developer agents that automate code implementation through intelligent planning and execution. Built with LangGraph multi-agent workflows
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) ⭐11398
  - TensorRT-LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and support state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs. TensorRT-LLM also contains components to create Python and C++ runtimes that orchestrate the inference execution in performant way.

### Rss
- [D4d4](https://www.nmichaels.org/musings/d4d4/d4d4/)
  - <a href="https://news.ycombinator.com/item?id=44932401">Comments</a>
- [Show HN: I replaced vector databases with Git for AI memory (PoC)](https://github.com/Growth-Kinetics/DiffMem)
  - <a href="https://news.ycombinator.com/item?id=44969622">Comments</a>
- [Code review can be better](https://tigerbeetle.com/blog/2025-08-04-code-review-can-be-better/)
  - <a href="https://news.ycombinator.com/item?id=44967469">Comments</a>
- [Universal Tool Calling Protocol (UTCP)](https://github.com/universal-tool-calling-protocol/python-utcp)
  - <a href="https://news.ycombinator.com/item?id=44939642">Comments</a>
- [Show HN: I was curious about spherical helix, ended up making this visualization](https://visualrambling.space/moving-objects-in-3d/)
  - <a href="https://news.ycombinator.com/item?id=44962066">Comments</a>

### Misc
- [eliza](https://github.com/elizaOS/eliza) ⭐16634
  - Autonomous agents for everyone
- [cline](https://github.com/cline/cline) ⭐49519
  - Autonomous coding agent right in your IDE, capable of creating/editing files, executing commands, using the browser, and more with your permission every step of the way.
- [AgentGPT](https://github.com/reworkd/AgentGPT) ⭐34785
  - 🤖 Assemble, configure, and deploy autonomous AI Agents in your browser.
- [khoj](https://github.com/khoj-ai/khoj) ⭐30761
  - Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents, schedule automations, do deep research. Turn any online or local LLM into your personal, autonomous AI (gpt, claude, gemini, llama, qwen, mistral). Get started - free.
- [gpt-researcher](https://github.com/assafelovic/gpt-researcher) ⭐23111
  - LLM based autonomous agent that conducts deep local and web research on any topic and generates a long report with citations.
- [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) ⭐21377
  - A list of AI autonomous agents
- [agenticSeek](https://github.com/Fosowl/agenticSeek) ⭐20906
  - Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. 🔔 Official updates only via twitter @Martin993886460 (Beware of fake account)
- [12-factor-agents](https://github.com/humanlayer/12-factor-agents) ⭐12811
  - What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers?
- [Announcing LocalLlama discord server & bot!](https://www.reddit.com/r/LocalLLaMA/comments/1mpk2va/announcing_localllama_discord_server_bot/)
  - <table> <tr><td> <a href="https://www.reddit.com/r/LocalLLaMA/comments/1mpk2va/announcing_localllama_discord_server_bot/"> <img alt="Announcing LocalLlama discord server &amp; bot!" src="https://b.thu
- [r/LocalLlama is looking for moderators](https://www.reddit.com/r/LocalLLaMA/comments/1mjf5ol/rlocalllama_is_looking_for_moderators/)
  - &#32; submitted by &#32; <a href="https://www.reddit.com/user/HOLUPREDICTIONS"> /u/HOLUPREDICTIONS </a> <br /> <span><a href="https://www.reddit.com/r/LocalLLaMA/application/">[link]</a></span> &#32; 
- [deepseek-ai/DeepSeek-V3.1 · Hugging Face](https://www.reddit.com/r/LocalLLaMA/comments/1mw3c7s/deepseekaideepseekv31_hugging_face/)
  - <table> <tr><td> <a href="https://www.reddit.com/r/LocalLLaMA/comments/1mw3c7s/deepseekaideepseekv31_hugging_face/"> <img alt="deepseek-ai/DeepSeek-V3.1 · Hugging Face" src="https://external-preview.r
- [My LLM trained from scratch on only 1800s London texts brings up a real protest from 1834](https://www.reddit.com/r/LocalLLaMA/comments/1mvnmjo/my_llm_trained_from_scratch_on_only_1800s_london/)
  - <table> <tr><td> <a href="https://www.reddit.com/r/LocalLLaMA/comments/1mvnmjo/my_llm_trained_from_scratch_on_only_1800s_london/"> <img alt="My LLM trained from scratch on only 1800s London texts brin
- [DeepSeek-V3.1 implements Anthropic API compatibility](https://www.reddit.com/r/LocalLLaMA/comments/1mw3nat/deepseekv31_implements_anthropic_api_compatibility/)
  - <table> <tr><td> <a href="https://www.reddit.com/r/LocalLLaMA/comments/1mw3nat/deepseekv31_implements_anthropic_api_compatibility/"> <img alt="DeepSeek-V3.1 implements Anthropic API compatibility" src
- [Generate Images with Claude and Hugging Face](https://huggingface.co/blog/claude-and-mcp)
  - No description
- [From Zero to GPU: A Guide to Building and Scaling Production-Ready CUDA Kernels](https://huggingface.co/blog/kernel-builder)
  - No description
- [TextQuests: How Good are LLMs at Text-Based Video Games?](https://huggingface.co/blog/textquests)
  - No description
- [Introducing AI Sheets: a tool to work with datasets using open AI models!](https://huggingface.co/blog/aisheets)
  - No description


<!-- AGENT-INFRA-END -->

---

## ⚡ Usage

- Explore projects under each category
- Check [agent_resources.md](./agent_resources.md) for the **full list**
- Follow the [CHANGELOG.md](./CHANGELOG.md) for new additions

---

## 🔄 Updates

- `README.md` → curated + auto-updated section  
- `agent_resources.md` → full categorized resources (auto-generated)  
- `CHANGELOG.md` → update history with timestamps

---

## 🤝 Contributing
Contributions are welcome! 🎉  
- Fork the repo  
- Add your project/resource under the correct category  
- Submit a PR  

Please follow the existing format:  

---

## 📜 License

[MIT](./LICENSE)

---

<p align="center">💡 Curated with ❤️ for the AI Agent community.</p>
