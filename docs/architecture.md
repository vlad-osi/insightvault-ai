# InsightVault AI Architecture

## Overview

InsightVault AI is a document intelligence platform based on RAG architecture.

## Components

### Frontend

Responsible for:

- User interface
- Document management
- AI chat interface

### Backend API

Built with FastAPI.

Responsibilities:

- Authentication
- Document upload
- Processing pipeline
- Search API

### Database

PostgreSQL stores:

- Users
- Documents
- Metadata
- Search indexes

### AI Pipeline

Document

↓

Text extraction

↓

Chunking

↓

Embeddings

↓

Vector Search

↓

LLM Response

## Future Architecture

Next.js
|
FastAPI
|
PostgreSQL + pgvector
|
Embedding Model
|
LLM
