from components.organisms.get_holiday_list import get_holiday_list
from components.organisms.copy_workbook import copy_workbook
from components.organisms.set_cells import set_cells


def process_workbook(
        year: str, month_padded: str, tmp_year_month_day: str, full_name: str,
        month_days_num: int, first_week_day: int):
    date_list = get_holiday_list(
        month_days_num, first_week_day, year, month_padded)
    wb_copy = copy_workbook(year, month_padded)
    set_cells(wb_copy, tmp_year_month_day, full_name, date_list)

    return wb_copy
