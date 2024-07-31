
# What to evaluate

If we have a simple LLM call without chat history, we can just have query and answer. Run the query through the LLM and compare the result with the ground truth answer. If we have a whole chat, we can still test every step of the chat separately by just attaching the chat history to the LLM calls.
# Constructing a dataset

Generally the dataset should just contain query and answer.