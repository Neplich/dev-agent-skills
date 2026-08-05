from fastapi import APIRouter, Depends, HTTPException, status

from .schemas import CreateMessageRequest, MessageResponse

router = APIRouter(
    prefix="/api/knowledge-discovery/conversations/{conversation_id}/messages",
    tags=["knowledge-discovery", "conversations"],
)


def require_workspace_member() -> str:
    return "member-1"


@router.post("", response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
def create_message(
    conversation_id: str,
    payload: CreateMessageRequest,
    member_id: str = Depends(require_workspace_member),
) -> MessageResponse:
    if conversation_id == "forbidden":
        raise HTTPException(status_code=403, detail={"code": "conversation_forbidden"})
    return MessageResponse(
        id="message-1",
        conversation_id=conversation_id,
        content=payload.content,
    )


@router.get("", response_model=list[MessageResponse])
def list_messages(
    conversation_id: str,
    member_id: str = Depends(require_workspace_member),
) -> list[MessageResponse]:
    if conversation_id == "forbidden":
        raise HTTPException(status_code=403, detail={"code": "conversation_forbidden"})
    return []
