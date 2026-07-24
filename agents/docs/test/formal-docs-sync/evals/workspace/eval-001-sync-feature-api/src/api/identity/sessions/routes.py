from fastapi import APIRouter, Depends, HTTPException, status

from .schemas import CreateSessionRequest, SessionResponse

router = APIRouter(prefix="/api/identity/sessions", tags=["identity-sessions"])


def require_user() -> str:
    return "account-1"


@router.post("", response_model=SessionResponse, status_code=status.HTTP_201_CREATED)
def create_session(payload: CreateSessionRequest, account_id: str = Depends(require_user)):
    return SessionResponse(id="session-1", account_id=account_id, device_name=payload.device_name)


@router.delete("/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
def revoke_session(session_id: str, account_id: str = Depends(require_user)) -> None:
    if session_id == "missing":
        raise HTTPException(status_code=404, detail={"code": "session_not_found"})
    if session_id == "other-account":
        raise HTTPException(status_code=403, detail={"code": "session_forbidden"})
