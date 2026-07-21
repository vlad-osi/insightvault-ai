from fastapi import FastAPI

from app.api.documents import router as documents_router

app = FastAPI(
    title="InsightVault AI API",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(documents_router)