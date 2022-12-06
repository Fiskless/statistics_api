from datetime import date

from sqlalchemy.orm import Session

from database.models import Statistic
from statistic.schemas import StatisticCreate, StatisticOut


def create_statistic(statistic: StatisticCreate, db: Session):
    db_statistic = Statistic(**statistic.dict())
    db.add(db_statistic)
    db.commit()
    db.refresh(db_statistic)
    return db_statistic


def get_statistic(start_date: date, end_date: date, db: Session):
    statistics = db.query(Statistic)\
        .filter(Statistic.date >= start_date, Statistic.date <= end_date) \
        .order_by(Statistic.date, Statistic.views) \
        .all()
    all_statistics = []
    for statistic in statistics:
        all_statistics.append(
            StatisticOut(
                date=statistic.date,
                views=statistic.views,
                clicks=statistic.clicks,
                cost=statistic.cost,
                cpc=statistic.get_average_click_cost,
                cpm=statistic.get_average_cost_thousand_views
            ))
    return all_statistics


def delete_statistic(db: Session):
    db.query(Statistic).delete()
    db.commit()