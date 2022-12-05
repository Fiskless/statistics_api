from pydantic import BaseModel, Field
from datetime import date


class StatisticCreate(BaseModel):
    date: date
    views: int = Field(None, ge=0)
    clicks: int = Field(None, ge=0)
    cost: float = Field(None, ge=0)

    class Config:
        orm_mode = True