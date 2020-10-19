from typing import Any
from pathlib import Path


def save_workbook(
        wb_copy: Any,
        last_name: str,
        year_month: str,
        year: str,
        month: str) -> None:
    file_name = f'勤務表{year_month}_{last_name}.xls'
    file_path = str(Path('./generated') / file_name)
    wb_copy.save(file_path)
    print(f'{year}年{month}月の勤務表作成に成功しました。')
