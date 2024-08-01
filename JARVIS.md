# Motivation

LLMs seem to get smaller and smaller. Currently large parts of LLM training is spent on remembering a bunch of internet data. But the goal seems to be more and  more to decouple the "intelligence" from the knowledge. This is mostly done by adjusting the training datasets and focusing on teaching materials instead of all of the internet.
Furthermore, decreasing the size of the model might keep the intelligence and lose some data memory because the model is forced generalize more.
If we get to a point however, where we have a pretty intelligent model without much memorized information, we will need to give the model tools to acquire this information.

Small models + RAG will most likely play a central role in the future of LLM applications. So we might as well focus on this right now, because this combination already has many applications and benefits over just normal LLMs.

- We can feed the model private data
- The model can add links to the actual data, so that the user can verify the validity of the answers
- The model can have up to date information

# Skills

Help with everything i am doing on my pc.
- Answer general questions about the current codebase
- Code completion
- 
# Context

Managing Context will be critical.
Should have context to everything that the programmer can look at.
- File system (read)
- Treesitter code structure/signature tree
- Access to current browser pages

# How

- Embed and store a variety of different data modalities in a vector database efficiently
	- Qdrant seems to be a nice choice
- Give LLM tools to access this vector database, filter and retrieve relevant vectors to the current context
	- model needs some "base" amount of information/knowledge know what to retrieve. There will be some balance of model size, intelligence and knowledge
	- immediate knowledge, e.g. the current file in coding or the current web page when in a browser should probably always be fully in the context
	- additionally there should be a summary of what is going on in the environment e.g. the file tree, the Treesitter code structure or what programs are running on the pc
- 