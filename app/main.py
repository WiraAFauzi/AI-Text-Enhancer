import os
from fastapi import FastAPI, HTTPException
from app.schemas import TextRequest, TextResponse
from app.services import generate_text

app = FastAPI(title="AI Text Enhancer API")


@app.get("/")
def health():
    return {"status": "running"}


@app.post("/generate", response_model=TextResponse)
def generate(request: TextRequest):
    try:
        result = generate_text(request.text, request.mode)

        # Detect if running in mock mode
        source = (
            "mock"
            if os.getenv("MOCK_MODE", "false").lower() == "true"
            else "openai"
        )

        return {
            "result": result,
            "source": source
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
