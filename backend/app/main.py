from fastapi import FastAPI


app = FastAPI(
    title="InsightVault AI API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "InsightVault AI API"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }