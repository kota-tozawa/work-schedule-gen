from typing import Tuple
import sys
from namedivider import NameDivider


def get_name() -> Tuple[str, str, str]:
    '''take full name as input and automatically divide it into last name and first name.'''
    flg = False
    while flg is False:
        try:
            fullname = input('勤務表に記載する氏名をフルネームを入力してください：')
            name_divider = NameDivider()
            divided_name = name_divider.divide_name(fullname)
            flg = True
        except ValueError:
            print('フルネームが未入力または正しくない形式で入力されました。')
            y_or_n = input('再入力しますか？[y/n]：')
            if (y_or_n == 'n'):
                sys.exit()

    print('divided_name.family', divided_name.family)
    print('divided_name.given', divided_name.given)
    print('fullname', fullname)
    return divided_name.family, divided_name.given, fullname


def get_last_or_first_name(last_name: bool = True) -> str:
    '''Set `last_name=False` to get first name.'''
    last_or_first_name = ''
    if last_name is True:
        last_or_first_name = 'あなたの苗字'
    else:
        last_or_first_name = 'あなたの名前'

    while True:
        name = input(
            f'{last_or_first_name}を入力してください：'
        )
        if (name == ''):
            print(
                f'{last_or_first_name}が未入力です。'
            )
            y_or_n = input(
                f'{last_or_first_name}を再入力しますか？[y/n]：'
            )
            if (y_or_n == 'n'):
                sys.exit()
        else:
            break
