
## Random Thoughs

- Run locally with small fast model to test
	- tinyllama is really fast
		- good for sanity checking bugs
		- but doesn't really follow prompts well
	- with decent gpu llama3 is probably best
		- still decently fast
		- follows prompts well
	- not sure what prompt/performance difference better models make, but i assume that the better the model, the better the whole system; it will probably be necessary to balance performance and cost at some point for specific agents
	- llama3:8b is not using the tools it is provided
- Function Calling
	- [Good article](https://towardsdatascience.com/llm-output-parsing-function-calling-vs-langchain-63b80545b3a7) about the differences between openai function calling and langchains output parser
	- function calling instructs the model in the system message to return in the specified format, but openai finetuned for that
		- "Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means functions count against the model's context limit and are billed as input tokens. If running into context limits, we suggest limiting the number of functions or the length of documentation you provide for function parameters. 
		- you can finetune with specific functions if you have a lot of functions that add to and thus limit your context size
	- with output parser you can specify the output format, add it to the prompt and parse the response with the same format

