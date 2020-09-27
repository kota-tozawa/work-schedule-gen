import sys
from datetime import datetime
from typing import Tuple

def get_last_or_first_name(last_name: bool = True) -> str:
    '''Set `last_name=False` to get first name'''
    last_or_first_name = ''
    if last_name == True:
        last_or_first_name = '苗字'
    else:
        last_or_first_name = '名前'

    while True:
        name = input('{last_or_first_name}を入力してください：'.format(last_or_first_name=last_or_first_name))
        if (name == ''):
            print('{last_or_first_name}が未入力です。'.format(last_or_first_name=last_or_first_name))
            y_or_n = input('{last_or_first_name}を再入力しますか？[y/n]：'.format(last_or_first_name=last_or_first_name))
            if (y_or_n == 'n'):
                sys.exit()
        else:
            break

    return name

def get_year_month() -> str:
    '''Returns yyyymm string'''
    while True:
        try:
            date = input('作成したい勤務表の年月を入力してください（例：202009）：')
            datetime.strptime(date, '%Y%m')
        except ValueError:
            print('不正な年月が入力されました。')
            y_or_n = input('年月を再入力しますか？[y/n]：')
            if (y_or_n == 'n'):
                sys.exit()
        except Exception as e:
            print(e)
            sys.exit()
        else:
            break

    insert_string_to_base = lambda base_string, insert_point, insert_string : \
    base_string[:insert_point] + insert_string + base_string[insert_point:]

    date = insert_string_to_base(date, 4, '0') if len(date) == 5 else date

    return date

def separate_year_month(year_month: str) -> Tuple[str, str]:
    '''yyyymm -> yyyy, mm'''
    year = year_month[0:4]
    month = ''
    if (year_month[4] == '0'):
        month = year_month[5:6]
    else:
        month = year_month[4:6]

    return year, month

def get_out_cell(out_sheet, col_index, row_index):
    """ Extract the internal xlwt cell representation. """
    row = out_sheet._Worksheet__rows.get(row_index)
    if not row: return None
    cell = row._Row__cells.get(col_index)

    return cell

def set_out_cell(out_sheet, col, row, value):
    """ Change cell value without changing formatting. """
    previous_cell = get_out_cell(out_sheet, col, row)
    out_sheet.write(row, col, value)
    if previous_cell:
        new_cell = get_out_cell(out_sheet, col, row)
        if new_cell:
            new_cell.xf_idx = previous_cell.xf_idx
