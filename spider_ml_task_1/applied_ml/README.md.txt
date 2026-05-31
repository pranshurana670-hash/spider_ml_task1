# Applied ML Domain Task – RAG Chatbot

## Objective

Build a Retrieval-Augmented Generation (RAG) chatbot capable of answering questions from a custom knowledge base.

---

## System Overview

The chatbot combines:

1. Information Retrieval
2. Vector Embeddings
3. Large Language Models

to provide context-aware responses.

---

## Pipeline

```text
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Retriever
    ↓
LLM
    ↓
Final Response
```

---

## Components Used

### Document Processing

* Text extraction
* Cleaning
* Chunking

### Embedding Model

Used to convert text chunks into vector representations.

### Vector Store

Stores embeddings and enables semantic search.

Examples:

* FAISS
* ChromaDB

### Retriever

Retrieves the most relevant chunks based on user queries.

### Language Model

Generates responses using retrieved context.

---

## Features

* Context-aware question answering
* Semantic search
* Retrieval-based response generation
* Reduced hallucination compared to standalone LLM responses
* Scalable knowledge base integration

---

## Project Structure

```text
chatbot_code/
│
├── ingestion.py
├── embeddings.py
├── retriever.py
├── chatbot.py
└── requirements.txt
```

(Actual file names may vary depending on implementation.)

---

## How to Run

1. Install dependencies.
2. Load documents.
3. Generate embeddings.
4. Build vector database.
5. Launch chatbot interface.
6. Ask questions related to the uploaded knowledge base.

---

## Learning Outcomes

This project helped me understand:

* Retrieval-Augmented Generation
* Embedding Models
* Vector Databases
* Semantic Search
* Prompt Engineering
* LLM-based Applications
* End-to-End Chatbot Development
