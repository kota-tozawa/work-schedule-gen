import calendar
from pathlib import Path
from xlrd import open_workbook
from xlwt import Font, Alignment, Borders, Formula, XFStyle
from xlutils.copy import copy
from modules.functional_components import get_last_or_first_name, get_year_month, separate_year_month
from modules.utils import set_out_cell

WEEK_DAYS = ['月', '火', '水', '木', '金', '土', '日']

# 氏名
last_name = get_last_or_first_name()
first_name = get_last_or_first_name(last_name=False)
full_name = last_name + first_name

# 年月
year_month = get_year_month()
year, month = separate_year_month(year_month)
year_month_day = '{year}/{month}/1'.format(year=year, month=month)
# calendar.monthrange(int(year), int(month))[0] は、0が月曜で、6が日曜
first_week_day, month_days_num = calendar.monthrange(int(year), int(month))
month_padded = '0' + month if len(month) == 1 else month

# 祝日判定用日付
for i in range(month_days_num):
    date = []


# 書式情報
# フォント
font_normal = Font()
font_normal.name = u'HG正楷書体-PRO'
font_red = Font()
font_red.name = u'HG正楷書体-PRO'
font_red.colour_index = 0x0A
# アラインメント
alignment = Alignment()
alignment.horz = Alignment.HORZ_CENTER
alignment.vert = Alignment.VERT_CENTER
# 通常のスタイル
style_normal = XFStyle()
style_normal.font = font_normal
style_normal.alignment = alignment
# 赤文字のスタイル
style_red = XFStyle()
style_red.font = font_red
style_red.alignment = alignment

# template.xls を開いて、日付や曜日、名前などを入れて、勤務表を生成
template_file = str(Path('./template.xls'))
wb = open_workbook(template_file, formatting_info=True, on_demand=True)
wb.get_sheet(0).name = u'【勤務表】{year}.{month}'.format(
    year=year, month=month_padded)
wb_copy = copy(wb)
out_sheet = wb_copy.get_sheet(0)
# タイトルに年月をセット
set_out_cell(out_sheet, 0, 0, year_month_day)
# 氏名をセット
out_sheet.write(2, 7, '氏名：' + full_name, style_normal)
# 日付・曜日をセット
for i in range(month_days_num):
    # 日付
    out_sheet.write(6 + i, 0, i + 1, style_normal)
    # 曜日
    if WEEK_DAYS[(first_week_day + i) % 7] in ['土', '日']:
        out_sheet.write(
            6 + i, 1, WEEK_DAYS[(first_week_day + i) % 7], style_red)
    else:
        out_sheet.write(
            6 + i, 1, WEEK_DAYS[(first_week_day + i) % 7], style_normal)

# 保存
file_name = '勤務表{year_month}_{last_name}.xls'.format(
    year_month=year_month, last_name=last_name)
file_path = str(Path('./generated') / file_name)
wb_copy.save(file_path)
print('勤務表の作成に成功しました。')
