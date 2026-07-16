from fastapi import APIRouter

router = APIRouter(prefix="/api/billing")


@router.get("/invoices")
def list_invoices():
    return {"items": []}
