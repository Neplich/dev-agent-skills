from fastapi import APIRouter, HTTPException, Query

from .schemas import SearchResponse

router = APIRouter(prefix="/api")


@router.get(
    "/search",
    response_model=SearchResponse,
    responses={400: {"description": "invalid_query"}},
)
def search(
    q: str = Query(..., description="Search text"),
    limit: int = Query(20, ge=1, le=100),
) -> SearchResponse:
    if not q.strip():
        raise HTTPException(
            status_code=400,
            detail={"code": "invalid_query", "message": "q must not be blank"},
        )
    items = [{"id": "doc-1", "title": f"Result for {q}"}][:limit]
    return SearchResponse(items=items, total=len(items))
