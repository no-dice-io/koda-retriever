# GoldenRetriever
This retriever is a custom fine-tunable Hybrid Retriever that dynamically determines the optimal alpha for a given query.
An LLM is used to categorize the query and therefore determine the optimal alpha value, as each category has a preset/provided alpha value.
It is recommended that you run tests on your corpus of data and queries to determine categories and corresponding alpha values for your use case.

### Disclaimer
*The default categories and alpha values are not recommended for production use*

## Introduction
Alpha tuning in hybrid retrieval for RAG models refers to the process of adjusting the weight (alpha) given to different components of a hybrid search strategy. In RAG, the retrieval component is crucial for fetching relevant context from a knowledge base, which the generation component then uses to produce answers. By fine-tuning the alpha parameter, the balance between the retrieved results from dense vector search methods (like embeddings) and traditional sparse methods (like TF-IDF) can be optimized. This optimization aims to enhance the overall performance of the system, ensuring that the retrieval process effectively supports the generation of accurate and contextually relevant responses.

### Simply explained
Imagine you're playing a game where someone whispers a sentence to you, and you have to decide whether to draw a picture of exactly what they said, or draw a picture of what you think they mean. Alpha tuning is like finding the best rule for when to draw exactly what's said and when to think deeper about the meaning. It helps us get the best mix, so the game is more fun and everyone understands each other better!

## Usage

```python
retriever = GoldenRetriever(
    index = vector_index
    , llm = service_context.llm
    , reranker = reranker
    , matrix = tuned_alpha_categories
    , verbose = True
)

query = "What is the capital of France?"

results = retriever.retrieve(query)
```

## Setup

### Quickstart
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### For testing/notebooks
```bash
pip install -r requirements.txt
pip install black dynaconf 
```

## Citations
Idea & original implementation sourced from the following docs:
- https://blog.llamaindex.ai/llamaindex-enhancing-retrieval-performance-with-alpha-tuning-in-hybrid-search-in-rag-135d0c9b8a00
- https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-ai-search-outperforming-vector-search-with-hybrid/ba-p/3929167

## Buy me a coffee 

[Thanks!](https://www.buymeacoffee.com/nodice)
