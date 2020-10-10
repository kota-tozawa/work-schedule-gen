from datetime import datetime
from typing import Tuple
import jpholiday


def insert_string_to_base(base_string: str, insert_point: int, insert_string: str) -> str:
    '''e.g.) 'ABCFG', 3, 'DE' ->  'ABCDEFG' '''
    return base_string[:insert_point] + insert_string + base_string[insert_point:]


def separate_year_month(year_month: str) -> Tuple[str, str]:
    '''yyyymm -> yyyy, mm'''
    year = year_month[0:4]
    month = ''
    if (year_month[4] == '0'):
        month = year_month[5:6]
    else:
        month = year_month[4:6]

    return year, month


def zero_padding(value: str) -> str:
    '''e.g.) 7 -> 07, 19 -> 19'''
    return '0' + value if len(value) == 1 else value


def to_year_month_day(year: str, month_padded: str, day_padded: str) -> str:
    '''yyyy, mm, dd -> yyyymmdd'''

    return year + month_padded + day_padded


def is_holiday(str_date: str) -> bool:
    '''Determines if yyyymmdd is a holiday or not'''
    date = datetime.strptime(str_date, '%Y%m%d')
    if date.weekday() >= 5 or jpholiday.is_holiday(date):
        return True
    else:
        return False


def _get_out_cell(out_sheet, row_index, col_index):
    ''' Extract the internal xlwt cell representation. '''
    row = out_sheet._Worksheet__rows.get(row_index)
    if not row:
        return None
    cell = row._Row__cells.get(col_index)

    return cell


def set_out_cell(out_sheet, row, col, value):
    ''' Change cell value without changing formatting. '''
    previous_cell = _get_out_cell(out_sheet, col, row)
    out_sheet.write(row, col, value)
    if previous_cell:
        new_cell = _get_out_cell(out_sheet, col, row)
        if new_cell:
            new_cell.xf_idx = previous_cell.xf_idx
