import sys
from datetime import datetime

def get_valid_input_name():
    while True:
        name = input('氏名を入力してください（例：野比のび太）：')
        if (name == ''):
            print('氏名が未入力です。')
            y_or_n = input('氏名を再入力しますか？[y/n]：')
            if (y_or_n == 'n'):
                sys.exit()
        else:
            break
    return name

def get_valid_input_date():
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
    return date