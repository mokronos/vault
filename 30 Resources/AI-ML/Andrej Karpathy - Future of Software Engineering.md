---
title: Andrej Karpathy - Future of Software Engineering
---

# Andrej Karpathy - Future of Software Engineering

## What still needs to be built

- Agent-native infrastructure: systems designed for agents first, not humans. Documentation, APIs, and workflows should answer: "what do I paste to my agent?" instead of only giving human step-by-step instructions.
- End-to-end automation layers: the ability to go from prompt -> build -> deploy -> integrate without manual configuration, for example no UI clicking for DNS, auth, or infra wiring.
- Sensor and actuator abstractions: clean interfaces for agents to observe the world through data ingestion and act on it through APIs, services, and transactions.
- LLM-legible systems: data formats, APIs, and environments optimized for model interaction, meaning structured, contextual, and self-describing.
- Custom RL environments for niche domains: many valuable and verifiable domains are still untouched. Whoever defines good feedback loops there can unlock strong performance through fine-tuning.
- Better evaluation and verification frameworks: especially beyond code and math, where outputs need to be scored reliably in messy domains.
- Improved agent reliability layers: guardrails, debugging loops, and coordination systems for handling jagged intelligence.
- Knowledge synthesis systems: tools that continuously ingest, restructure, and recompile information into personal or organization-level living wikis.

## What software engineers and data scientists should focus on

- Spec and system design over implementation: define clear constraints, invariants, and architecture. Think in terms of what should happen, not only how to code it.
- Agent orchestration: multi-agent workflows, tool use, delegation patterns, and managing stochastic systems with feedback loops.
- Verification-first thinking: design problems so outputs can be tested or scored. Build eval harnesses, not just models or code.
- Working with jagged systems: assume inconsistency and add redundancy, checks, and recovery paths.
- Prompting and context engineering at scale: structure inputs, memory, and tool interfaces. Treat context as the program.
- Data and RL leverage: for data science, creating datasets, feedback signals, and fine-tuning pipelines becomes more valuable than model architecture work.
- Taste and judgment: recognize good and bad outputs in design, UX, code quality, and reasoning. Agents do not reliably optimize for this yet.
- Abstraction awareness: understand the underlying systems, such as data structures, compute, and efficiency, even if most low-level code is generated.
- End-to-end ownership: go from idea -> spec -> agent-built system -> validation -> deployment.
- Tooling mastery: use agent-based development environments deeply, not only at the surface level.

## Bottom line

Shift from writing code to designing systems that agents execute, with a strong emphasis on evaluation, control, and high-level reasoning.
