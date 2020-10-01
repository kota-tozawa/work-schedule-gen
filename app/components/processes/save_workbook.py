from typing import Any
from pathlib import Path


def save_workbook(wb_copy: Any, year_month: str, year: str, month: str, last_name: str) -> None:
    file_name = '勤務表{year_month}_{last_name}.xls'.format(
        year_month=year_month, last_name=last_name)
    file_path = str(Path('./generated') / file_name)
    wb_copy.save(file_path)
    print('{year}年{month}月の勤務表作成に成功しました。'.format(year=year, month=month))
