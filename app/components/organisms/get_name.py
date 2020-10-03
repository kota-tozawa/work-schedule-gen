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
            '{last_or_first_name}を入力してください：'.format(
                last_or_first_name=last_or_first_name
            )
        )
        if (name == ''):
            print(
                '{last_or_first_name}が未入力です。'.format(
                    last_or_first_name=last_or_first_name
                )
            )
            y_or_n = input(
                '{last_or_first_name}を再入力しますか？[y/n]：'.format(
                    last_or_first_name=last_or_first_name
                )
            )
            if (y_or_n == 'n'):
                sys.exit()
        else:
            break

    return name
