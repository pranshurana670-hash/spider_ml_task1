from utils.retriever import (
    get_similarity_retriever,
    get_mmr_retriever
)


COMPARISON_KEYWORDS = [
    "difference",
    "compare",
    "comparison",
    "versus",
    "vs"
]


def retrieve_chunks(question):

    question_lower = question.lower()

    is_comparison = any(
        keyword in question_lower
        for keyword in COMPARISON_KEYWORDS
    )

    if is_comparison:

        print("\nUsing MMR Retrieval")

        retriever = get_mmr_retriever()

    else:

        print("\nUsing Similarity Retrieval")

        retriever = get_similarity_retriever()

    docs = retriever.invoke(question)

    return docs