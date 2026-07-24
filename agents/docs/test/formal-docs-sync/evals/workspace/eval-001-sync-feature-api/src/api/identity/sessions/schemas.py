from pydantic import BaseModel, Field


class CreateSessionRequest(BaseModel):
    device_name: str = Field(min_length=1, max_length=80)


class SessionResponse(BaseModel):
    id: str
    account_id: str
    device_name: str
