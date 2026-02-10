from fastapi import FastAPI
from backend.app.routes import health, upload, query

app = FastAPI(
    title="Research Co-Pilot",
    description="AI-powered research assistant using RAG",
    version="1.0.0"
)

app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(query.router, prefix="/query", tags=["Query"])

@app.get("/")
def root():
    return {"message": "Research Co-Pilot API is live 🚀"}
