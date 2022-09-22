import datetime
from typing import Optional

from pydantic import BaseModel


class LinkBase(BaseModel):
    url: str


class Link(BaseModel):
    id: int
    status: Optional[str]
    created_at: datetime.datetime

    class Config:
        orm_mode = True


class LinkCreate(BaseModel):
    pass


class LinkUpdate(BaseModel):
    status: str
