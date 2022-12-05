from .router import router
from .schemas import StatisticCreate


@router.post('/save/')
def save_statistic(statistic: StatisticCreate):
    return statistic


@router.get('/get/')
def show_statistic(statistic: StatisticCreate):
    return statistic