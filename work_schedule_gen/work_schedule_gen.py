from datetime import datetime
import calendar
import xlrd
import xlwt
from xlutils.copy import copy
from functions import get_valid_input_date, get_valid_input_name

WEEK_DAYS = ('月', '火', '水', '木', '金', '土', '日')

input_name = get_valid_input_name()
input_date = get_valid_input_date()

wb = xlrd.open_workbook('template/template.xls')


# calendar.monthrange(2020,9)