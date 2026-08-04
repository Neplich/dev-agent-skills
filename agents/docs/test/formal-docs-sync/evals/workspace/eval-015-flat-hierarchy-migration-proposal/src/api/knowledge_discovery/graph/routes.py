from fastapi import APIRouter

router = APIRouter(prefix="/api/knowledge-discovery", tags=["knowledge-discovery"])


@router.post("/graph/search")
def search_graph() -> dict[str, list[object]]:
    return {"entities": [], "relationships": []}
