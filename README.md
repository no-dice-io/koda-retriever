![build-workflow](https://github.com/no-dice-io/koda-retriever/actions/workflows/python-app.yml/badge.svg) 

# Koda Retriever
This retriever is a custom fine-tunable Hybrid Retriever that dynamically determines the optimal alpha for a given query.
An LLM is used to categorize the query and therefore determine the optimal alpha value, as each category has a preset/provided alpha value.
It is recommended that you run tests on your corpus of data and queries to determine categories and corresponding alpha values for your use case.

![koda-retriever-mascot](https://i.imgur.com/224ocIw.jpeg)

### Disclaimer
*The default categories and alpha values are not recommended for production use*

## Introduction
Alpha tuning in hybrid retrieval for RAG models refers to the process of adjusting the weight (alpha) given to different components of a hybrid search strategy. In RAG, the retrieval component is crucial for fetching relevant context from a knowledge base, which the generation component then uses to produce answers. By fine-tuning the alpha parameter, the balance between the retrieved results from dense vector search methods and traditional sparse methods can be optimized. This optimization aims to enhance the overall performance of the system, ensuring that the retrieval process effectively supports the generation of accurate and contextually relevant responses.

### Simply explained
Imagine you're playing a game where someone whispers a sentence to you, and you have to decide whether to draw a picture of exactly what they said, or draw a picture of what you think they mean. Alpha tuning is like finding the best rule for when to draw exactly what's said and when to think deeper about the meaning. It helps us get the best mix, so the game is more fun and everyone understands each other better!

## Usage Snapshot

```python
retriever = KodaRetriever(
    index = vector_index
    , llm = Settings.llm
    , reranker = reranker
    , matrix = tuned_alpha_categories
    , verbose = True
)

query = "What is the capital of France?"

results = retriever.retrieve(query)
```

### Prerequisites
- [OpenAI API Key](https://platform.openai.com/overview)  *(default)* OR a Llama Index representation of whatever model you want to provide
- [Pinecone API Key](https://www.pinecone.io/) *(just for testing)*

*The OpenAI API Key is not necessary for usage of the retriever itself if you plan on using an Open Source model - but your tests will fail for now*

## Setup

### Quickstart
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

### Testing

```bash
# You'll need to set your environment variables
# This requires: An OpenAI API Key + Pinecone API Key
# Start w/ 'Quickstart' steps above

pip install pytest

export KODA_OPENAI_API_KEY="<openai_api_key_here>" # Necessary for the retriever itself
export KODA_PINECONE_API_KEY="<pinecone_api_key_here>" # Necessary for the retriever itself
```

## Documentation
Given that Koda Retriever is built ontop of and within the LLama Index ecosystem, documentation will largely be contained within Jupyter notebooks. Koda Retriever is compatible with all other retrieval interfaces and objects that would normally be able to interact with a LI-native retriever. The patterns and pre-requistes are almost entirely Llama Index based, so you may need to [start with Llama Index](https://docs.llamaindex.ai/en/stable/module_guides/querying/retriever/root.html) before really taking advantage of this retriever.

Please see the [documentation](./docs/) folder for more specific examples.

## Citations
Idea & original implementation sourced from the following docs:
- https://blog.llamaindex.ai/llamaindex-enhancing-retrieval-performance-with-alpha-tuning-in-hybrid-search-in-rag-135d0c9b8a00
- https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-ai-search-outperforming-vector-search-with-hybrid/ba-p/3929167

## Buy me a coffee 

[Thanks!](https://www.buymeacoffee.com/nodice)
