from fastapi import APIRouter

router = APIRouter(prefix="/api/knowledge-building", tags=["knowledge-building"])


@router.post("/documents", status_code=202)
def ingest_document() -> dict[str, str]:
    return {"id": "ingestion-1"}
