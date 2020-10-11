import pytest
from components.processes.process_workbook import process_workbook


@pytest.mark.integtest
def test_process_workbook():
    # 正常
    assert process_workbook('範馬勇次郎', '2020', '09',
                            '2020/9/1', 30, 1) is not None
