# WhyBack

WhyBack is an AI-powered e-commerce return intelligence platform that helps businesses understand **why products are being returned** and what they can change to reduce future returns.

## Problem

E-commerce businesses often know how many products are being returned, but they do not always understand the real root causes.

WhyBack will analyze return data, customer feedback, product information, and external product evidence to identify:

- High-return products
- Recurring customer complaints
- Likely root causes
- Financial impact
- Evidence-backed recommendations

## Planned AI Capabilities

- AI root-cause analysis
- LLM-powered business assistant
- RAG over business data
- Vector search with pgvector
- AI recommendations
- Skyvern-powered external product investigation
- Competitor listing analysis
- Evaluation and confidence scoring

## Planned Tech Stack

- Python
- FastAPI
- PostgreSQL
- pgvector
- LLMs
- Skyvern
- Docker

## Project Status

🚧 Currently under active development.

## Current Milestone

### Milestone 1 — Product Foundation

Current progress:

- [x] GitHub repository created
- [x] Initial project structure created
- [x] Python virtual environment created
- [x] FastAPI backend created
- [x] Health endpoint created
- [x] Routes, services, and models structure created
- [ ] PostgreSQL database integration
- [ ] Sample e-commerce returns dataset
- [ ] Frontend dashboard
- [ ] Frontend-backend integration
- [ ] Basic tests and validation

## Backend Architecture

```text
backend/
├── main.py
├── routes/
│   ├── __init__.py
│   └── health.py
├── services/
│   ├── __init__.py
│   └── health_service.py
├── models/
│   ├── __init__.py
│   └── health.py
└── __init__.py
```
## Backend Setup

### 1. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn backend.main:app --reload
```
