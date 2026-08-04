from fastapi import APIRouter

router = APIRouter(prefix="/api/knowledge-building", tags=["knowledge-building"])


@router.patch("/documents/{document_id}")
def curate_document(document_id: str) -> dict[str, str]:
    return {"id": document_id}
