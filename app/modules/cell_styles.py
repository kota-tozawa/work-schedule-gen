from xlwt import Font, Alignment, Pattern, Borders, Formula, XFStyle, Style


# 書式情報
# フォント
font_black = Font()
font_black.name = u'HG正楷書体-PRO'
font_red = Font()
font_red.name = u'HG正楷書体-PRO'
font_red.colour_index = Style.colour_map['red']
font_blue = Font()
font_blue.name = u'HG正楷書体-PRO'
font_blue.colour_index = Style.colour_map['blue']
# アラインメント
alignment = Alignment()
alignment.horz = Alignment.HORZ_CENTER
alignment.vert = Alignment.VERT_CENTER
# セルの背景色
pattern_grey = Pattern()
pattern_grey.pattern = Pattern.SOLID_PATTERN
pattern_grey.pattern_fore_colour = Style.colour_map['grey25']
# 枠線
borders_black = Borders()
borders_black.left = Borders.THIN
borders_black.right = Borders.THIN
borders_black.top = Borders.THIN
borders_black.bottom = Borders.THIN
# 黒文字白背景のスタイル
STYLE_BLACK_WHITE = XFStyle()
STYLE_BLACK_WHITE.font = font_black
STYLE_BLACK_WHITE.alignment = alignment
STYLE_BLACK_WHITE.borders = borders_black
# 黒文字白背景のスタイル（枠線なし）
STYLE_BLACK_WHITE_NO_BORDERS = XFStyle()
STYLE_BLACK_WHITE_NO_BORDERS.font = font_black
STYLE_BLACK_WHITE_NO_BORDERS.alignment = alignment
# 黒文字灰色背景のスタイル
STYLE_BLACK_GREY = XFStyle()
STYLE_BLACK_GREY.font = font_black
STYLE_BLACK_GREY.alignment = alignment
STYLE_BLACK_GREY.pattern = pattern_grey
STYLE_BLACK_GREY.borders = borders_black
# 赤文字灰色背景のスタイル
STYLE_RED_GREY = XFStyle()
STYLE_RED_GREY.font = font_red
STYLE_RED_GREY.alignment = alignment
STYLE_RED_GREY.pattern = pattern_grey
STYLE_RED_GREY.borders = borders_black
# 青文字灰色背景のスタイル
STYLE_BLUE_GREY = XFStyle()
STYLE_BLUE_GREY.font = font_blue
STYLE_BLUE_GREY.alignment = alignment
STYLE_BLUE_GREY.pattern = pattern_grey
STYLE_BLUE_GREY.borders = borders_black
