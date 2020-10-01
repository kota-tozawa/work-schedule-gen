from xlrd import open_workbook
from xlutils.copy import copy
from components.atoms.constants import TEMPLATE_FILE_PATH


def copy_workbook(year: str, month_padded: str):
    wb = open_workbook(TEMPLATE_FILE_PATH,
                       formatting_info=True, on_demand=True)
    wb.get_sheet(0).name = u'【勤務表】{year}.{month}'.format(
        year=year, month=month_padded)
    wb_copy = copy(wb)

    return wb_copy
