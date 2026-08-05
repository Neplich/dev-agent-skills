from fastapi import APIRouter

router = APIRouter(prefix="/api/platform-governance", tags=["platform-governance"])


@router.get("/workspaces")
def list_workspaces() -> list[dict[str, str]]:
    return []
