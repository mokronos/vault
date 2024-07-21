https://www.reddit.com/r/LocalLLaMA/comments/1cm6u9f/local_web_ui_with_actually_decent_rag/

## Rag vs Finetuning

Rag is like reading from a cheat sheet. Finetuning is long term studying. With Rag you will be able to have mostly accurate information, but the broader context might be hidden, like studying quickly before a test or just checking a cheat sheet for specific information. Finetuning actually incorporates the information into the model's thinking, but it might be a bit fuzzy at times.

A combination of both is probably best.




[[ml_glossary#Sample Space |Sample Space]]






# Overview

Rag takes the query that is sent by the user, embedds it, uses similarity search to find a similar vector in a vector store, retrieves this vector and adds that vector in text form to the query to give to the LLM

# Indexing

