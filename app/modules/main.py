from datetime import datetime
from pathlib import Path
import calendar
from xlrd import open_workbook
from xlutils.copy import copy
from xlutils.save import save
from functions import get_year_month, get_last_or_first_name, convert_year_month_to_year, convert_year_month_to_month

WEEK_DAYS = ['月', '火', '水', '木', '金', '土', '日']

last_name = get_last_or_first_name()
first_name = get_last_or_first_name(last_name=False)
full_name = last_name + first_name
year_month = get_year_month()
year = convert_year_month_to_year(year_month)
month = convert_year_month_to_month(year_month)
first_week_day, month_days_num = calendar.monthrange(int(year), int(month))
print(calendar.monthrange(int(year), int(month))) # first_week_dayは、0が月曜

# template.xls を開いて、日付や曜日、名前などを入れて、勤務表を生成
template_file = Path('../template.xls')
template_file = str(template_file)
wb = open_workbook(template_file, formatting_info=True)
wb_copy = copy(wb)
wb_copy.get_sheet(0).write(2, 7, '氏名：' + full_name)

# 保存
file_name = '勤務表{year_month}_{last_name}.xls'.format(year_month=year_month, last_name=last_name)
tmp_file_path = Path.cwd().parent
file_path = str(tmp_file_path/'generated'/file_name)
file_path = str(file_path)
wb_copy.save(file_path)
