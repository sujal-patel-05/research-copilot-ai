from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def query(question: str):
    return {
        "question": question,
        "answer": "RAG pipeline coming soon 🚀"
    }
