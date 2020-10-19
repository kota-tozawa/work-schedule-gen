import sys


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

    return name
