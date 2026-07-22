from fastapi import APIRouter, Depends, Header, HTTPException, Query
from pydantic import BaseModel

router = APIRouter(prefix="/api/billing", tags=["billing"])


class InvoiceList(BaseModel):
    items: list[str]
    total: int


def require_billing_reader(x_billing_role: str = Header(...)) -> str:
    if x_billing_role != "reader":
        raise HTTPException(status_code=403, detail={"code": "billing_forbidden"})
    return x_billing_role


@router.get("/invoices", response_model=InvoiceList)
def list_invoices(
    limit: int = Query(20, ge=1, le=100),
    _: str = Depends(require_billing_reader),
) -> InvoiceList:
    items = ["invoice-1"][:limit]
    return InvoiceList(items=items, total=len(items))
