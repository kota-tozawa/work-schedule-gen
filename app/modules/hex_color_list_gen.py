from pathlib import Path
from xlwt import Workbook, Pattern, XFStyle

# xlwtで利用可能な全ての色をxlsファイル上で表示する
# （参考：https://github.com/python-excel/xlwt/blob/master/xlwt/Style.py）
# TODO 関数「to_hex_int()」はここでしか使わないであろうから、utilsではなく一旦ここに置いておく


def to_hex_int(hex_str: str) -> int:
    '''Converts a hex string to hex number'''
    hex_int = int(hex_str, 16)
    return hex_int


# xlwtで利用可能な色を一括表示する用のスタイル
style_test_list = []
# 0x0(0)から0xff(255)までの色
for i in range(256):
    hex_str = hex(i)
    hex_int = to_hex_int(hex_str)
    pattern_test = Pattern()
    pattern_test.pattern = Pattern.SOLID_PATTERN
    pattern_test.pattern_fore_colour = hex_int
    style_test = XFStyle()
    style_test = XFStyle()
    style_test.pattern = pattern_test
    style_test_list.append(style_test)

# 色表示用xlsファイル
wb_test = Workbook()
ws_test = wb_test.add_sheet("colors available in xlwt")

# 色をセルの背景色にセット
ws_test.write(0, 0, "xlwtで利用可能な色の一覧")
for i in range(256):
    text = 'decimal: {dec}, hexadecimal: {hex}'.format(dec=str(i), hex=hex(i))
    ws_test.write(i + 1, 0, text, style_test_list[i])

# xlsファイルをtemplateディレクトリに保存
file_name = 'hex_color_list.xls'
file_path = str(Path('../template') / file_name)
wb_test.save(file_path)
