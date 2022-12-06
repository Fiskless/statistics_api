from pydantic import BaseModel, Field, validator
from datetime import date


class StatisticCreate(BaseModel):
    date: date
    views: int = Field(None, ge=0)
    clicks: int = Field(None, ge=0)
    cost: float = Field(None, ge=0)

    class Config:
        orm_mode = True

    @validator('cost')
    def check_cost_accuracy(cls, value):
        return float("{:.2f}".format(value))


class StatisticOut(StatisticCreate):
    cpc: float = Field(None, ge=0)
    cpm: float = Field(None, ge=0)

    @validator('cpc')
    def check_cpc_accuracy(cls, value):
        return float("{:.2f}".format(value))

    @validator('cpm')
    def check_cpm_accuracy(cls, value):
        return float("{:.2f}".format(value))


