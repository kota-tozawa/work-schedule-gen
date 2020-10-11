import pytest
from components.organisms.copy_workbook import copy_workbook


@pytest.mark.integtest
def test_copy_workbook():
    # 正常
    assert copy_workbook('2020', '09') is not None
    assert copy_workbook('2019', '12') is not None
