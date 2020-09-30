from pathlib import Path
from xlwt import Workbook, Pattern, XFStyle

# TODO 関数「to_hex_int()」はここでしか使わないであろうから、utilsではなく一旦ここに置いておく


def to_hex_int(hex_str: str) -> int:
    '''Converts a hex string to hex number'''
    hex_int = int(hex_str, 16)
    return hex_int


# 目的の色を探すための一括表示用スタイル
style_test_list = []
hex_list = []
# 0x0(0)から0xfe(255)まで
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
    hex_list.append(hex_int)

# 色表示用xlsファイル
wb_test = Workbook()
ws_test = wb_test.add_sheet("255 colors")

# 色をセット
for i in range(256):
    text = 'decimal: {dec}, hexadecimal: {hex}'.format(dec=str(i), hex=hex(i))
    ws_test.write(i, 0, text, style_test_list[i])

# 255色入りxlsファイルをgeneratedディレクトリに保存
file_name = 'hex_color_list.xls'
file_path = str(Path('../template') / file_name)
wb_test.save(file_path)
