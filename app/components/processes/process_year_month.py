import calendar
from typing import Tuple
from components.molecules.functions import separate_year_month, zero_padding
from components.organisms.get_year_month import get_year_month


def process_year_month() -> Tuple[str, str, str, str, str, int, int]:
    year_month = get_year_month()
    year, month = separate_year_month(year_month)
    tmp_year_month_day = '{year}/{month}/1'.format(year=year, month=month)
    month_padded = zero_padding(month)
    # calendar.monthrange(int(year), int(month))[0] は、0が月曜で、6が日曜
    first_week_day, month_days_num = calendar.monthrange(int(year), int(month))

    return year_month, year, month, tmp_year_month_day, month_padded, first_week_day, month_days_num
