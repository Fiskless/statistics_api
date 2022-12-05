from sqlalchemy import Column, Date, Integer, Float

from .database import Base


class Statistic(Base):
    __tablename__ = "statistic"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    views = Column(Integer, default=None)
    clicks = Column(Integer, default=None)
    cost = Column(Float, default=None)
