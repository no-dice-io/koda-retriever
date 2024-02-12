from config import settings
from llama_index.llms import AzureOpenAI
from llama_index.vector_stores import PGVectorStore
from llama_index import ServiceContext, VectorStoreIndex, Document
from llama_index.embeddings import OpenAIEmbedding, AzureOpenAIEmbedding
from llama_index.postprocessor import LLMRerank
from llama_index.indices.vector_store import VectorStoreIndex
from golden_retriever import GoldenRetriever
import pytest

# finish this later
# fix this later - merge it with llama hub and you can fix everything from there

@pytest.fixture
def setup() -> dict:
    """Pytest fixture to set up the GoldenRetriever and its dependencies"""

    service_context = ServiceContext.from_defaults(
        embed_model=AzureOpenAIEmbedding(
            model="text-embedding-ada-002",
            azure_deployment="text-embedding-ada-002",
            azure_endpoint=str(settings.openai_api_base),
            api_version=str(settings.azure_openai_api_version),
            api_key=str(settings.azure_openai_api_key),
        ),
        llm=AzureOpenAI(
            model="gpt-4",
            azure_deployment="gpt-4",
            azure_endpoint=str(settings.azure_openai_api_base),
            api_version=str(settings.azure_openai_api_version),
            api_key=str(settings.azure_openai_api_key),
        ),
    )

    shots = AlphaMatrix(data=DEFAULT_CATEGORIES)

    vector_index = VectorStoreIndex.from_documents(
        [Document.example()]
        , service_context=service_context
    )

    reranker = LLMRerank(service_context=service_context)

    retriever = GoldenRetriever(
        index=vector_index,
        llm=service_context.llm,
        reranker=reranker,
        matrix=shots,
        verbose=True,
    )

    return {
        "retriever": retriever,
        "service_context": service_context,
        "vector_index": vector_index,
        "matrix": shots,
    }
