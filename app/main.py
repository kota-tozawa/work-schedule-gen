from pathlib import Path
import calendar
from xlrd import open_workbook
from xlutils.copy import copy
from modules.functions import *

WEEK_DAYS = ['月', '火', '水', '木', '金', '土', '日']

last_name = get_last_or_first_name()
first_name = get_last_or_first_name(last_name=False)
full_name = last_name + first_name

year_month = get_year_month()
year, month = separate_year_month(year_month)
first_week_day, month_days_num = calendar.monthrange(int(year), int(month)) # calendar.monthrange(int(year), int(month))[0] は、0が月曜で、6が日曜

# template.xls を開いて、日付や曜日、名前などを入れて、勤務表を生成
template_file = str(Path('./template.xls'))
wb = open_workbook(template_file, formatting_info=True, on_demand=True)
wb_copy = copy(wb)
out_sheet = wb_copy.get_sheet(0)
set_out_cell(out_sheet, 2, 7, '氏名：' + full_name) # .write(2, 7, '氏名：' + full_name)


# 保存
file_name = '勤務表{year_month}_{last_name}.xls'.format(year_month=year_month, last_name=last_name)
file_path = str(Path('./generated') / file_name)
wb_copy.save(file_path)
print('勤務表の作成に成功しました。')
