import datetime
from datetime import date

from fastapi import Depends
from sqlalchemy.orm import Session

from database.database import SessionLocal
from . import crud
from .router import router
from .schemas import StatisticCreate, StatisticOut


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/save/')
def add_statistic(statistic: StatisticCreate, db: Session = Depends(get_db)):
    db_statistic = crud.create_statistic(statistic, db)
    return db_statistic


@router.get('/get/', response_model=list[StatisticOut])
def get_statistic(start_date: date = datetime.date.today(),
                  end_date: date = datetime.date.today(),
                  db: Session = Depends(get_db)):
    statistic_out = crud.get_statistic(start_date, end_date, db)
    return statistic_out


@router.delete('/delete/')
def delete_statistic(db: Session = Depends(get_db)):
    crud.delete_statistic(db)
    return