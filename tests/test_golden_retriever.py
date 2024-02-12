from asyncio import run
from . import GoldenRetriever

def test_init(setup):

    retriever = setup.get("retriever")

    assert retriever.index is not None, "index should not be None"
    assert retriever.llm is not None, "llm should not be None"
    assert isinstance(
        retriever, GoldenRetriever
    ), "retriever should be an instance of GoldenRetriever"


def test_retrieve(setup):

    retriever = setup.get("retriever")
    query = "Why should I use semantic search to rank results?"
    results = retriever.retrieve(query)

    assert isinstance(results, list), "retrieve should return a list"


def test_a_retrieve(setup):

    retriever = setup.get("retriever")
    query = "Why should I use semantic search to rank results?"
    results = run(retriever.aretrieve(query))

    assert isinstance(results, list), "aretrieve should return a list"


def test_categorize(setup):

    retriever = setup.get("retriever")
    expected_categories = setup.get("matrix").get_categories()

    query = "Why should I use semantic search to rank results?"
    category = retriever.categorize(query)

    assert isinstance(category, str), "categorize should return a string"
    assert (
        category in expected_categories
    ), "categorize should return a category from the matrix"


def test_category_retrieve(setup):

    retriever = setup.get("retriever")
    query = "Why should I use semantic search to rank results?"
    category = "concept seeking query"

    results = retriever.category_retrieve(category, query)

    assert isinstance(results, list), "category_retrieve should return a list"
