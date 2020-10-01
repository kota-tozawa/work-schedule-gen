from xlwt import easyxf


# xlwtで使用可能な色の一覧
# https://docs.google.com/spreadsheets/d/1ihNaZcUh7961yU7db1-Db0lbws4NT24B7koY8v8GHNQ/pubhtml?gid=1072579560&single=true

# 黒文字,白背景のスタイル
STYLE_BLACK_WHITE = easyxf(
    'font: name HG正楷書体-PRO;'
    'align: vert centre, horiz center;'
    'pattern: pattern solid, fore_colour white;'
    'borders: left thin, right thin, top thin, bottom thin;')

# 黒文字,白背景のスタイル（枠線なし）
STYLE_BLACK_WHITE_NO_BORDERS = easyxf(
    'font: name HG正楷書体-PRO;'
    'align: vert centre, horiz center;'
    'pattern: pattern solid, fore_colour white;')

# 黒文字,灰色背景のスタイル
STYLE_BLACK_GREY = easyxf(
    'font: name HG正楷書体-PRO;'
    'align: vert centre, horiz center;'
    'pattern: pattern solid, fore_colour grey25;'
    'borders: left thin, right thin, top thin, bottom thin;')

# 青文字,灰色背景のスタイル
STYLE_BLUE_GREY = easyxf(
    'font: name HG正楷書体-PRO, colour blue;'
    'align: vert centre, horiz center;'
    'pattern: pattern solid, fore_colour grey25;'
    'borders: left thin, right thin, top thin, bottom thin;')

# 赤文字,灰色背景のスタイル
STYLE_RED_GREY = easyxf(
    'font: name HG正楷書体-PRO, colour red;'
    'align: vert centre, horiz center;'
    'pattern: pattern solid, fore_colour grey25;'
    'borders: left thin, right thin, top thin, bottom thin;')
