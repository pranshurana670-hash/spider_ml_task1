from langchain_community.vectorstores import FAISS
from utils.embeddings import get_embeddings


def load_vectorstore():

    db = FAISS.load_local(
        "vectorstore",
        get_embeddings(),
        allow_dangerous_deserialization=True
    )

    return db


def get_similarity_retriever():

    db = load_vectorstore()

    return db.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 4
        }
    )


def get_mmr_retriever():

    db = load_vectorstore()

    return db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 6,
            "fetch_k": 20
        }
    )