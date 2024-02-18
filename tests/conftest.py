from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.postprocessor import LLMRerank
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core import Settings
from koda_retriever import KodaRetriever, AlphaMatrix, DEFAULT_CATEGORIES
import pytest
import os
from pinecone import Pinecone
from dynaconf import Dynaconf

CONFIG = Dynaconf(
    # export envvars with `export KODA_FOO=bar`, then access with `CONFIG.foo`
    envvar_prefix="KODA"
)


@pytest.fixture
def setup() -> dict:
    """Pytest fixture to set up the KodaRetriever and its dependencies"""

    os.environ["OPENAI_API_KEY"] = CONFIG.openai_api_key

    pc = Pinecone(api_key=CONFIG.pinecone_api_key)
    index = pc.Index("sample-movies")

    Settings.llm = OpenAI()
    Settings.embed_model = OpenAIEmbedding()

    vector_store = PineconeVectorStore(pinecone_index=index, text_key="summary")
    vector_index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store, embed_model=Settings.embed_model
    )

    shots = AlphaMatrix(data=DEFAULT_CATEGORIES)

    reranker = LLMRerank(llm=Settings.llm)

    retriever = KodaRetriever(
        index=vector_index,
        llm=Settings.llm,
        reranker=reranker,
        matrix=shots,
        verbose=True,
    )

    return {
        "retriever": retriever,
        "llm": Settings.llm,
        "reranker": reranker,
        "embed_model": Settings.embed_model,
        "vector_index": vector_index,
        "matrix": shots,
    }
