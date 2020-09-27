import sys
from datetime import datetime

def get_last_or_first_name(last_name: bool = True) -> str:
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

def convert_year_month_to_year(year_month: str) -> str:
    return year_month[0:4]

def convert_year_month_to_month(year_month: str) -> str:
    if (year_month[4] == '0'):
        return year_month[5:6]
    else:
        return year_month[4:6]
