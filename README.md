# InsightVault AI

AI-powered knowledge base platform for teams.

InsightVault AI allows users to upload documents, search knowledge semantically, and interact with internal information using Retrieval-Augmented Generation (RAG).

## Features

Current:

- ✅ FastAPI backend
- ✅ PostgreSQL database
- ✅ SQLAlchemy ORM
- ✅ Alembic migrations
- ✅ Document upload API
- ✅ Document management

Roadmap:

- 🔄 Next.js frontend
- 🔄 PDF text extraction
- 🔄 Document chunking
- 🔄 Embeddings pipeline
- 🔄 Vector search with pgvector
- 🔄 AI chat assistant
- 🔄 Authentication
- 🔄 CI/CD
- 🔄 Production deployment

## Architecture

Frontend
|
|
FastAPI Backend
|
|
PostgreSQL + pgvector
|
|
AI Pipeline

## Tech Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic

### Frontend

- Next.js
- React
- Tailwind CSS

## Local Development

Backend:

```bash
cd backend

uvicorn app.main:app --reload

API documentation:
http://localhost:8000/docs

Project Status
MVP development stage.

License
MIT

```
