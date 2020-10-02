from components.atoms.constants import WEEK_DAYS
from components.molecules.classes import Date
from components.molecules.functions import (
    zero_padding,
    to_year_month_day,
    is_holiday
)


def get_holiday_list(month_days_num: int, first_week_day: int, year: str, month_padded: str) -> list:
    date_list = []
    for i in range(month_days_num):
        day = i + 1
        day_padded = zero_padding(str(day))
        week_day = WEEK_DAYS[(first_week_day + i) % 7]
        date = to_year_month_day(year, month_padded, day_padded)
        holiday_flg = is_holiday(date)
        dt = Date(day, week_day, holiday_flg)
        date_list.append(dt)

    return date_list
