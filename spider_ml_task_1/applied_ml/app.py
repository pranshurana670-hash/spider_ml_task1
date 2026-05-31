import time
import streamlit as st

from utils.retrieve import retrieve_chunks
from utils.context_builder import build_context
from utils.prompt_template import build_prompt
from utils.llm import generate_answer


# -----------------------------------
# Query Classification
# -----------------------------------

def classify_query(question):

    comparison_keywords = [
        "difference",
        "differences",
        "compare",
        "comparison",
        "versus",
        "vs",
        "better",
        "advantages",
        "disadvantages",
        "pros",
        "cons"
    ]

    question = question.lower()

    for keyword in comparison_keywords:

        if keyword in question:
            return "Comparison", "MMR"

    return "Fact-Based", "Similarity"


# -----------------------------------
# Streamlit Config
# -----------------------------------

st.set_page_config(
    page_title="Research Paper RAG",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Research Paper RAG Assistant")

st.markdown(
    """
Ask questions about your research papers using
Retrieval-Augmented Generation (RAG).
"""
)

# -----------------------------------
# Sidebar
# -----------------------------------

with st.sidebar:

    st.header("System Information")

    st.write("Embedding Model")
    st.code("all-MiniLM-L6-v2")

    st.write("Vector Database")
    st.code("FAISS")

    st.write("LLM")
    st.code("google/flan-t5-base")

    st.write("Retrieval")
    st.code("Similarity + MMR")

    st.divider()

    st.header("Example Questions")

    st.markdown("""
- What is BERT?
- What is GPT?
- What problem does RAG solve?
- How does LoRA reduce training cost?
- Difference between BERT and GPT
- Compare RAG and GPT
- How does self-attention work?
""")

# -----------------------------------
# User Question
# -----------------------------------

question = st.text_input(
    "Enter your question:"
)

ask_button = st.button("Ask Question")

# -----------------------------------
# Main Logic
# -----------------------------------

if ask_button:

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        query_type, retrieval_method = classify_query(
            question
        )

        # ----------------------------
        # Retrieval
        # ----------------------------

        retrieval_start = time.time()

        docs = retrieve_chunks(question)

        retrieval_time = (
            time.time() - retrieval_start
        )

        # ----------------------------
        # Context
        # ----------------------------

        context = build_context(docs)

        # ----------------------------
        # Prompt
        # ----------------------------

        prompt = build_prompt(
            context=context,
            question=question
        )

        # ----------------------------
        # Generation
        # ----------------------------

        generation_start = time.time()

        answer = generate_answer(prompt)

        generation_time = (
            time.time() - generation_start
        )

        # ----------------------------
        # Sources
        # ----------------------------

        sources = sorted(
            set(
                doc.metadata.get(
                    "source",
                    "Unknown"
                )
                for doc in docs
            )
        )

        # ----------------------------
        # Confidence
        # ----------------------------

        if len(sources) >= 3:
            confidence = "High"

        elif len(sources) == 2:
            confidence = "Medium"

        else:
            confidence = "Low"

        # ----------------------------
        # Query Information
        # ----------------------------

        st.subheader("Query Details")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Query Type",
                query_type
            )

        with col2:
            st.metric(
                "Retrieval",
                retrieval_method
            )

        with col3:
            st.metric(
                "Confidence",
                confidence
            )

        # ----------------------------
        # Timing
        # ----------------------------

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Retrieval Time",
                f"{retrieval_time:.2f}s"
            )

        with col2:
            st.metric(
                "Generation Time",
                f"{generation_time:.2f}s"
            )

        # ----------------------------
        # Answer
        # ----------------------------

        st.subheader("Answer")

        st.write(answer)

        # ----------------------------
        # Sources
        # ----------------------------

        st.subheader("Sources Used")

        for source in sources:

            st.success(source)

        # ----------------------------
        # Retrieved Chunks
        # ----------------------------

        st.subheader("Retrieved Chunks")

        for i, doc in enumerate(
            docs,
            start=1
        ):

            source = doc.metadata.get(
                "source",
                "Unknown"
            )

            chunk_id = doc.metadata.get(
                "chunk_id",
                "N/A"
            )

            with st.expander(
                f"Chunk {i} | {source} | ID: {chunk_id}"
            ):

                st.write(
                    doc.page_content
                )

        # ----------------------------
        # Prompt Viewer (Debug)
        # ----------------------------

        with st.expander(
            "View Prompt (Debug)"
        ):

            st.code(prompt)