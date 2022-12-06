from sqlalchemy import Column, Date, Integer, Float
from sqlalchemy.ext.hybrid import hybrid_property

from .database import Base


class Statistic(Base):
    __tablename__ = "statistic"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)
    views = Column(Integer, default=None)
    clicks = Column(Integer, default=None)
    cost = Column(Float, default=None)

    @hybrid_property
    def get_average_click_cost(self):
        try:
            cpc = self.cost/self.clicks
        except ZeroDivisionError:
            cpc = 0
        return cpc

    @hybrid_property
    def get_average_cost_thousand_views(self):
        try:
            cpm = self.cost / self.views * 1000
        except ZeroDivisionError:
            cpm = 0
        return cpm