from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import transactions, receipts, reports, auth

app = FastAPI(
    title="Ledgero API",
    version="1.0.0"
)

# ✅ CORS (Allow Netlify frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to Netlify URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root route
@app.get("/")
def root():
    return {"status": "Ledgero API is running"}

# ✅ Health check (Render likes this)
@app.get("/health")
def health():
    return {"status": "healthy"}

# ✅ Routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(transactions.router, prefix="/api/transactions", tags=["transactions"])
app.include_router(receipts.router, prefix="/api/receipts", tags=["receipts"])
app.include_router(reports.router, prefix="/api/reports", tags=["reports"])
