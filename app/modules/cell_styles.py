from xlwt import Font, Alignment, Pattern, Borders, Formula, XFStyle


# 書式情報
# フォント
font_black = Font()
font_black.name = u'HG正楷書体-PRO'
font_red = Font()
font_red.name = u'HG正楷書体-PRO'
font_red.colour_index = 0x0A
# アラインメント
alignment = Alignment()
alignment.horz = Alignment.HORZ_CENTER
alignment.vert = Alignment.VERT_CENTER
# セルの背景色
pattern_grey = Pattern()
pattern_grey.pattern = Pattern.SOLID_PATTERN
pattern_grey.pattern_fore_colour = 0x15
# 黒文字白背景のスタイル
STYLE_BLACK_WHITE = XFStyle()
STYLE_BLACK_WHITE.font = font_black
STYLE_BLACK_WHITE.alignment = alignment
# 黒文字灰色背景のスタイル
STYLE_BLACK_GREY = XFStyle()
STYLE_BLACK_GREY.font = font_black
STYLE_BLACK_GREY.alignment = alignment
STYLE_BLACK_GREY.pattern = pattern_grey
# 赤文字灰色背景のスタイル
STYLE_RED_GREY = XFStyle()
STYLE_RED_GREY.font = font_red
STYLE_RED_GREY.alignment = alignment
STYLE_RED_GREY.pattern = pattern_grey
