def _get_out_cell(out_sheet, row_index, col_index,):
    """ Extract the internal xlwt cell representation. """
    row = out_sheet._Worksheet__rows.get(row_index)
    if not row: return None
    cell = row._Row__cells.get(col_index)

    return cell

def set_out_cell(out_sheet, row, col, value):
    """ Change cell value without changing formatting. """
    previous_cell = _get_out_cell(out_sheet, col, row)
    out_sheet.write(row, col, value)
    if previous_cell:
        new_cell = _get_out_cell(out_sheet, col, row)
        if new_cell:
            new_cell.xf_idx = previous_cell.xf_idx