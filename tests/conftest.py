from config import settings
from llama_index.llms import AzureOpenAI
from llama_index.vector_stores import PGVectorStore
from llama_index import ServiceContext
from llama_index.embeddings import AzureOpenAIEmbedding
from llama_index.postprocessor import LLMRerank
from llama_index.indices.vector_store import VectorStoreIndex
from . import (
    GoldenRetriever,
    AlphaMatrix,
    DEFAULT_CATEGORIES,
)
import pytest


@pytest.fixture
def setup() -> dict:
    """Pytest fixture to set up the GoldenRetriever and its dependencies"""

    service_context = ServiceContext.from_defaults(
        embed_model=AzureOpenAIEmbedding(
            model="text-embedding-ada-002",
            azure_deployment="text-embedding-ada-002",
            azure_endpoint=str(settings.azure_openai_api_base),
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

    vector_index = VectorStoreIndex.from_vector_store(
        vector_store=PGVectorStore.from_params(
            host=str(settings.pgvector_host),
            port=str(settings.pgvector_port),
            user=str(settings.pgvector_user),
            password=str(settings.pgvector_password),
            database=str(settings.pgvector_database),
            schema_name=str(settings.pgvector_schema),
            table_name="vector_store",
            embed_dim=1536,
            hybrid_search=True,
        ),
        service_context=service_context,
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
