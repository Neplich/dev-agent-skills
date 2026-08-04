from fastapi import APIRouter

router = APIRouter(prefix="/api/platform-governance", tags=["platform-governance"])


@router.get("/jobs/{job_id}")
def get_job(job_id: str) -> dict[str, str]:
    return {"id": job_id, "status": "completed"}
