from llama_index.llms import OpenAI
from llama_index import ServiceContext, VectorStoreIndex, Document
from llama_index.embeddings import OpenAIEmbedding
from llama_index.postprocessor import LLMRerank
from llama_index.indices.vector_store import VectorStoreIndex
from llama_index.vector_stores import PineconeVectorStore
from koda_retriever import KodaRetriever, AlphaMatrix, DEFAULT_CATEGORIES
import pytest
import os
from pinecone import Pinecone
from dynaconf import Dynaconf

SETTINGS = Dynaconf(
    # export envvars with `export KODA_FOO=bar`, then access with `SETTINGS.foo`
    envvar_prefix="KODA"
)


@pytest.fixture
def setup() -> dict:
    """Pytest fixture to set up the KodaRetriever and its dependencies"""

    os.environ["OPENAI_API_KEY"] = str(SETTINGS.openai_api_key)

    pc = Pinecone(api_key=SETTINGS.pinecone_api_key)
    index = pc.Index("sample-movies")

    service_context = ServiceContext.from_defaults(
        embed_model=OpenAIEmbedding(model="text-embedding-ada-002"),
        llm=OpenAI(model="gpt-3.5-turbo"),
    )

    vector_store = PineconeVectorStore(pinecone_index=index, text_key="summary")
    print(vector_store)
    vector_index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store, service_context=service_context
    )

    shots = AlphaMatrix(data=DEFAULT_CATEGORIES)

    reranker = LLMRerank(service_context=service_context)

    retriever = KodaRetriever(
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
