
# Random stuff

## Chat history

Originally i though that to call an LLM Chat model API i would just have to take the chat history and the roles for each message and align them in a string like this:

```Python
prompt = f"""
System: ...
User: What is an apple?
Assistant: It is a fruit.
User: What color is it?
"""
```

And then you just send this string to the API. But this isn't how the API's work. They take a list of chat messages (with roles) and then create this string internally to call the LLM. So we can't be sure how OpenAI for example exactly constructs the final prompt.