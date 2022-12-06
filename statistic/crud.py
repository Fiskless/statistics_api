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
        .filter(Statistic.date >= start_date, Statistic.date <= end_date)\
        .all()
    all_statistics = []
    for statistic in statistics:
        try:
            cpc = statistic.cost / statistic.clicks
        except ZeroDivisionError:
            cpc = 0
        try:
            cpm = statistic.cost / statistic.views * 1000
        except ZeroDivisionError:
            cpm = 0
        all_statistics.append(
            StatisticOut(
                date=statistic.date,
                views=statistic.views,
                clicks=statistic.clicks,
                cost=statistic.cost,
                cpc=cpc,
                cpm=cpm
            ))
    return all_statistics


def delete_statistic(db: Session):
    db.query(Statistic).delete()
    db.commit()