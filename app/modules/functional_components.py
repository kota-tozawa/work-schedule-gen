import sys
from datetime import datetime
from modules.utils import insert_string_to_base


def get_last_or_first_name(last_name: bool = True) -> str:
    '''Set `last_name=False` to get first name.'''
    last_or_first_name = ''
    if last_name is True:
        last_or_first_name = '苗字'
    else:
        last_or_first_name = '名前'

    while True:
        name = input('{last_or_first_name}を入力してください：'.format(
            last_or_first_name=last_or_first_name))
        if (name == ''):
            print('{last_or_first_name}が未入力です。'.format(
                last_or_first_name=last_or_first_name))
            y_or_n = input(
                '{last_or_first_name}を再入力しますか？[y/n]：'.format(last_or_first_name=last_or_first_name))
            if (y_or_n == 'n'):
                sys.exit()
        else:
            break

    return name


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
