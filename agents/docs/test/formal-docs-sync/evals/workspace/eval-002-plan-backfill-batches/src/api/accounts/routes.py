from fastapi import APIRouter, HTTPException

from .schemas import AccountResponse

router = APIRouter(prefix="/api/accounts")


@router.get("/{account_id}", response_model=AccountResponse)
def get_account(account_id: str) -> AccountResponse:
    if account_id == "missing":
        raise HTTPException(status_code=404, detail={"code": "account_not_found"})
    return AccountResponse(id=account_id, display_name="Example", active=True)
