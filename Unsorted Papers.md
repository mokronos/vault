
# MULTI-AGENT COLLABORATION: HARNESSING THE POWER OF INTELLIGENT LLM AGENTS

[Link](https://arxiv.org/pdf/2306.03314)

## Basic Idea

- Multi agent system as graph
	- Agents as Node
	- Plugins (Tools) as Nodes
	- Edges are messages/communication channels
- Agents can have different tasks and roles
	- Agents themselves can have the ability to create and halt other agents
	- Planning agents
	- Specialized task agents
	- Have state, which has some history of the conversation and relevant information
- Tools/Plugins need exact description of things one can do with it
	- Functionalities (which actions the agent can perform)
	- Config and Constraints
- Messages
	- Have some content (string)
	- Some action, which can specify what prompt should be used with the content, or how it should be used with the tool

I think actions are always encoded in some form of prompt, so you need to tell the agent that it can use certain tools like "You can use a calculator by answering with "\[calculator] 2+3". Then this can be parsed and we can run the calculation and give it with the original prompt as the answer to the LLM.

---

## System Design

- Halting and Supervision
	- One agent can oversee other agents doing some task and halt them if they get stuck in a loop or just don't achieve the goal
	- An oracle agent can just look at the original prompt and verify is certain "thoughts" of agents seem to be going in the correct direction for achieving the correct outcome
- System design Agent
	- Could overview the whole system, or even full launch all the agents needed for the system
	- Remove the need for Task specific setup by just letting the first agent design the setup
- Need to externally limit agent creation, to not overload the system or introduce inefficiencies
	- monitor current load and give it to system design agent
	- analyze the tasks of all existing agents before adding new ones to limit overlapping tasks
- Finetuning vs RAG
	- Finetuning would be nicer for things like legal theory for a judge or lawyer agent. Otherwise one runs out of context length, when adding all of legal theory and case law to the system message or prompt.
	- But for more rare or things that need to be up to date, like currency exchange, using a plugin might be better. This can be just searching specific things on the internet or retrieving things from a database or a vector database.
---
## Applications

- Case Studies
	- Court Simulation
		- Training for law students
		- Testing new legal theories
	- Software Development

## Paper Critique

- too many repetitions; mentions way too many times that by combining multiple agents you can achieve better performance; "enabling efficient collaboration and interaction among the agents"

# Gorilla: Large Language Model Connected with Massive APIs

[Link](https://arxiv.org/pdf/2305.15334)

# Small LLMs Are Weak Tool Learners: A Multi-LLM Agent

[Link](https://arxiv.org/pdf/2401.07324)

# More Agents Is All You Need

[Link](https://arxiv.org/pdf/2402.05120)