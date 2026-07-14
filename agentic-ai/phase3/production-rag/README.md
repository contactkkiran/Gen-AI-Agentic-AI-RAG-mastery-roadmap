# Production RAG Project

This folder contains a production-ready variant of the FastAPI Retrieval-Augmented Generation application.

## Folder structure

- `app/`
  - `main.py` — FastAPI entry point.
  - `database/` — PostgreSQL connection and query logging.
  - `rag/` — PDF ingestion, chunking, and vector store creation.
  - `agent/` — Agent orchestration and retrieval tool.
  - `models/` — Request schemas.
- `data/` — Source documents for ingestion.
- `chroma_db/` — Persisted vector embeddings.
- `requirements.txt` — Dependencies.

## Purpose

- Provide a RAG application that accepts user queries.
- Retrieve relevant content from PDF or documents.
- Use a LangChain agent to combine retrieval context with an LLM response.
- Persist query and response history in PostgreSQL.

## Setup

1. Create a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install fastapi uvicorn psycopg2-binary langchain langchain-openai langchain-chroma chromadb PyMuPDF
```

3. Start the application:

```bash
uvicorn app.main:app --reload
```

4. Visit swagger docs:

```
http://127.0.0.1:8000/docs
```

## Important Notes

- Ensure the PostgreSQL database credentials are configured securely.
- `chroma_db/` is the persisted vector store directory and may be generated or updated when the app runs.
- Replace the OpenAI model or API settings as needed for your environment.
