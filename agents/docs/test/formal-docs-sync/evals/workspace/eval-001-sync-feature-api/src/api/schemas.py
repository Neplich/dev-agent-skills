from pydantic import BaseModel


class SearchItem(BaseModel):
    id: str
    title: str


class SearchResponse(BaseModel):
    items: list[SearchItem]
    total: int


class ErrorResponse(BaseModel):
    code: str
    message: str
