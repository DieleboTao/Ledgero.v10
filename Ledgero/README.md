# Ledgero

This is a minimal starter for Ledgero (backend FastAPI + frontend React/Vite).

## Run locally with Docker Compose

1. Build and start services:
```bash
docker-compose up --build
```

2. Create DB tables (dev quick route):
```bash
docker-compose exec backend python -c "from app.db import engine; from app.models import Base; Base.metadata.create_all(bind=engine); print('tables created')"
```

3. Open:
- Frontend: http://localhost:3000
- Backend docs: http://localhost:8000/docs

## What I included
- Backend: FastAPI endpoints for receipts upload, transactions CRUD, reports (P&L CSV).
- Frontend: React + Vite simple app with upload receipt, transactions list, and reports page.
- Dockerfiles and docker-compose for local dev.

## Notes
I cannot publish a public live preview from here. To get a public preview quickly, deploy the repo to Railway, Render, or DigitalOcean (instructions in earlier chat).

