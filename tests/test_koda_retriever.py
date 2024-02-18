from asyncio import run
from koda_retriever import KodaRetriever


def test_init(setup):

    retriever = setup.get("retriever")

    assert retriever.index is not None, "index should not be None"
    assert retriever.llm is not None, "llm should not be None"
    assert isinstance(
        retriever, KodaRetriever
    ), "retriever should be an instance of KodaRetriever"


def test_retrieve(setup):

    retriever = setup.get("retriever")
    query = "How many Jurassic Park movies are there?"
    results = retriever.retrieve(query)

    assert isinstance(results, list), "retrieve should return a list"


def test_a_retrieve(setup):

    retriever = setup.get("retriever")
    query = "How many Jurassic Park movies are there?"
    results = run(retriever.aretrieve(query))

    assert isinstance(results, list), "aretrieve should return a list"


def test_categorize(setup):

    retriever = setup.get("retriever")
    expected_categories = setup.get("matrix").get_categories()

    query = "What are LLMs good at?"
    category = retriever.categorize(query)

    assert isinstance(category, str), "categorize should return a string"
    assert (
        category in expected_categories
    ), "categorize should return a category from the matrix"


def test_category_retrieve(setup):

    retriever = setup.get("retriever")
    query = "What are LLMs good at?"
    category = "concept seeking query"

    results = retriever.category_retrieve(category, query)

    assert isinstance(results, list), "category_retrieve should return a list"
