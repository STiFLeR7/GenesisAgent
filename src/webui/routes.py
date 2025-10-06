from fastapi import APIRouter
from src.storage.persistence import fetch_top

router = APIRouter(prefix="/api", tags=["dashboard"])

@router.get("/top")
def get_top_ideas(limit: int = 5):
    data = fetch_top(limit)
    return {"ideas": [{"content": c, "score": s} for c, s in data]}
