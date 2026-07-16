from pydantic import BaseModel


class AccountResponse(BaseModel):
    id: str
    display_name: str
    active: bool
