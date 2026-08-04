from fastapi import APIRouter

router = APIRouter(prefix="/api/knowledge-discovery", tags=["knowledge-discovery"])


@router.post("/conversations", status_code=201)
def create_conversation() -> dict[str, str]:
    return {"id": "conversation-1"}
