from typing import Any
from components.molecules.functions import set_out_cell
from components.atoms.cell_styles import (
    STYLE_BLACK_WHITE,
    STYLE_BLACK_WHITE_NO_BORDERS,
    STYLE_BLUE_GREY,
    STYLE_RED_GREY,
    STYLE_RIGHT_BORDER
)


def set_cells(
        wb_copy: Any,
        tmp_year_month_day: str,
        full_name: str,
        date_list: list) -> None:
    # ワークブック（template.xls）の一番最初のシートを取得
    out_sheet = wb_copy.get_sheet(0)
    # タイトルに年月をセット
    set_out_cell(out_sheet, 0, 0, tmp_year_month_day)
    # 氏名をセット
    out_sheet.write(2, 7, '氏名：{full_name}'.format(
        full_name=full_name), STYLE_BLACK_WHITE_NO_BORDERS)
    # 日付・曜日をセット
    grey_row_list = []
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
            grey_row_list.append(row)
        else:
            out_sheet.write(
                row, col, week_day, STYLE_BLACK_WHITE)
    # 休日・祝日の行に背景灰色のセルをセット
    for row in grey_row_list:
        for col in range(2, 8):
            out_sheet.write(row, col, '', STYLE_BLUE_GREY)

    # 一番右の枠線が表示されない事象の対応
    for row in range(4, 38):
        col = 9
        out_sheet.write(row, col, '', STYLE_RIGHT_BORDER)
