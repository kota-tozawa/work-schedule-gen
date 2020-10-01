import sys
from datetime import datetime
from components.molecules.functions import insert_string_to_base


def get_year_month() -> str:
    '''Returns yyyymm string.'''
    while True:
        try:
            date = input('作成したい勤務表の年月を入力してください（例：202009, 20209）：')
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

    date = insert_string_to_base(
        date, 4, '0') if len(date) == 5 else date

    return date
