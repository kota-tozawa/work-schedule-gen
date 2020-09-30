import calendar
from pathlib import Path
from xlrd import open_workbook
from xlutils.copy import copy
from modules.cell_styles import STYLE_BLACK_WHITE, STYLE_BLACK_GREY, STYLE_RED_GREY
from modules.classes import Date
from modules.constants import WEEK_DAYS
from modules.functional_components import get_last_or_first_name, get_year_month
from modules.utils import separate_year_month, zero_padding, to_year_month_day, is_holiday, set_out_cell


# 氏名
last_name = get_last_or_first_name()
first_name = get_last_or_first_name(last_name=False)
full_name = last_name + first_name

# 年月
year_month = get_year_month()
year, month = separate_year_month(year_month)
tmp_year_month_day = '{year}/{month}/1'.format(year=year, month=month)
# calendar.monthrange(int(year), int(month))[0] は、0が月曜で、6が日曜
first_week_day, month_days_num = calendar.monthrange(int(year), int(month))
month_padded = zero_padding(month)

# 祝日含む休日判定用の日付リスト
date_list = []
for i in range(month_days_num):
    day = i + 1
    day_padded = zero_padding(str(day))
    week_day = WEEK_DAYS[(first_week_day + i) % 7]
    date = to_year_month_day(year, month_padded, day_padded)
    holiday_flg = is_holiday(date)
    dt = Date(day, week_day, holiday_flg)
    date_list.append(dt)

# template.xls を開いて、日付や曜日、名前などを入れて、勤務表を生成
template_file = str(Path('./template/template.xls'))
wb = open_workbook(template_file, formatting_info=True, on_demand=True)
wb.get_sheet(0).name = u'【勤務表】{year}.{month}'.format(
    year=year, month=month_padded)
wb_copy = copy(wb)
out_sheet = wb_copy.get_sheet(0)
# タイトルに年月をセット
set_out_cell(out_sheet, 0, 0, tmp_year_month_day)
# 氏名をセット
out_sheet.write(2, 7, '氏名：{full_name}'.format(
    full_name=full_name), STYLE_BLACK_WHITE)
# 日付・曜日をセット
for dt in date_list:
    # 日付
    row = 5 + dt.get_day()
    col = 0
    day = dt.get_day()
    out_sheet.write(row, col, day, STYLE_BLACK_WHITE)
    # 曜日
    col = 1
    week_day = dt.get_week_day()
    if dt.get_holiday_flg() is True:
        out_sheet.write(
            row, col, week_day, STYLE_RED_GREY)
    else:
        out_sheet.write(
            row, col, week_day, STYLE_BLACK_WHITE)

# 保存
file_name = '勤務表{year_month}_{last_name}.xls'.format(
    year_month=year_month, last_name=last_name)
file_path = str(Path('./generated') / file_name)
wb_copy.save(file_path)
print('{year}年{month}月の勤務表作成に成功しました。'.format(year=year, month=month))
