https://www.reddit.com/r/LocalLLaMA/comments/1cm6u9f/local_web_ui_with_actually_decent_rag/
https://www.reddit.com/r/LocalLLaMA/comments/16cbimi/yet_another_rag_system_implementation_details_and/
https://huggingface.co/learn/cookbook/en/agent_rag
## Rag vs Finetuning

Rag is like reading from a cheat sheet. Finetuning is long term studying. With Rag you will be able to have mostly accurate information, but the broader context might be hidden, like studying quickly before a test or just checking a cheat sheet for specific information. Finetuning actually incorporates the information into the model's thinking, but it might be a bit fuzzy at times.

A combination of both is probably best.


[[ml_glossary#Sample Space |Sample Space]]


# Overview

Rag takes the query that is sent by the user, embeds it, uses similarity search to find a similar vector in a vector store, retrieves this vector and adds that vector in text form to the query to give to the LLM.

# Indexing

![[Excalidraw/Drawing 2024-08-13 23.16.06.excalidraw.md]]
# Rag improvements

## Citations

 https://arxiv.org/pdf/2305.14627
 Just put this in system prompt:
> `Write an accurate, engaging, and concise answer for the given question using only the provided search results (some of which might be irrelevant) and cite them properly. Use an unbiased and journalistic tone. Always cite for any factual claim. When citing several search results, use [1][2][3]. Cite at least one document and at most three documents in each sentence. If multiple documents support the sentence, only cite a minimum sufficient subset of the documents.`

## HyDE

https://arxiv.org/pdf/2212.10496

Tell the LLM to create a hypothetical document that might answer the current question. Then use that document in the similarity search of the vector database.

## Chain/Setup

tool_calling_agent

## Prompting

https://www.reddit.com/r/LocalLLaMA/comments/1bii8or/open_llm_prompting_principle_what_you_repeat_will/
## Where to abstract

There are different levels in a system at which you can say, im just gonna use an api and not deal with it.

In our case, we use the API of an LLM. The different providers, Ollama and OpenAI have a similar API. What this abstracts:
- Dealing with running a GPU for inference
- Dealing with model structure and the corresponding inference code
- 