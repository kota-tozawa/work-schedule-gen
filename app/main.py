import sys
from components.organisms.get_name import get_name
from components.processes.process_name import process_name
from components.processes.process_workbook import process_workbook
from components.processes.process_year_month import process_year_month
from components.processes.save_workbook import save_workbook


# 引数「-f」があるときはフルネームのみ入力すればOK
if __name__ == '__main__':
    args = sys.argv
    if len(args) == 0:
        name_input = process_name
    elif args[1] == '-f':
        name_input = get_name


# 氏名
last_name, first_name, full_name = name_input()

# 年月
year_month, year, month, tmp_year_month_day, month_padded, first_week_day, month_days_num = process_year_month()

# 氏名、年月などを入れて、勤務表を生成
wb_copy = process_workbook(
    full_name, year, month_padded,
    tmp_year_month_day, month_days_num, first_week_day
)

# 生成された勤務表を保存
save_workbook(wb_copy, last_name, year_month, year, month)
