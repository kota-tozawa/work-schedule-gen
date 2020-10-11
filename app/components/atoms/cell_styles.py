from xlwt import easyxf


# xlwtで使用可能な色の一覧
# https://docs.google.com/spreadsheets/d/1ihNaZcUh7961yU7db1-Db0lbws4NT24B7koY8v8GHNQ/pubhtml?gid=1072579560&single=true

# TODO template.xlsの背景色の灰色が再現できない。一番近いgrey25で代用
# 黒文字,白背景のスタイル
STYLE_BLACK_WHITE = easyxf(
    'font: name HG正楷書体-PRO, height 220;'
    'align: vert centre, horiz center;'
    'pattern: pattern solid, fore_colour white;'
    'borders: left thin, right thin, top thin, bottom thin;'
)

# 黒文字,白背景のスタイル（枠線なし）
STYLE_BLACK_WHITE_NO_BORDERS = easyxf(
    'font: name HG正楷書体-PRO, height 220;'
    'align: vert centre, horiz center;'
    'pattern: pattern solid, fore_colour white;'
)

# 黒文字,白背景のスタイル（14pt）
# 14 * 20 = 280
STYLE_BLACK_WHITE_BIGGER = easyxf(
    'font: name HG正楷書体-PRO, height 280;'
    'align: vert centre, horiz center;'
    'pattern: pattern solid, fore_colour white;'
)

# 黒文字,灰色背景のスタイル
STYLE_BLACK_GREY = easyxf(
    'font: name HG正楷書体-PRO, height 220;'
    'align: vert centre, horiz center;'
    'pattern: pattern solid, fore_colour grey25;'
    'borders: left thin, right thin, top thin, bottom thin;'
)

# 青文字,灰色背景のスタイル
STYLE_BLUE_GREY = easyxf(
    'font: name HG正楷書体-PRO, colour blue, height 220;'
    'align: vert centre, horiz center;'
    'pattern: pattern solid, fore_colour grey25;'
    'borders: left thin, right thin, top thin, bottom thin;'
)

# 赤文字,灰色背景のスタイル
STYLE_RED_GREY = easyxf(
    'font: name HG正楷書体-PRO, colour red, height 220;'
    'align: vert centre, horiz center;'
    'pattern: pattern solid, fore_colour grey25;'
    'borders: left thin, right thin, top thin, bottom thin;'
)

# 表の一番右の枠線を表示するためのスタイル
STYLE_RIGHT_BORDER = easyxf(
    'borders: left thin;'
)

# TODO 実働時間合計用の白文字, 白背景スタイル
STYLE_WHITE_WHITE = easyxf(
    'font: color white'
)
