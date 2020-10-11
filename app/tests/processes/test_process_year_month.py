import pytest
from components.processes.process_year_month import process_year_month


@pytest.mark.integtest
def test_process_year_month(monkeypatch):
    # 正常
    monkeypatch.setattr('builtins.input', lambda _: '202009')
    monkeypatch.setattr(
        'components.organisms.get_year_month.get_year_month', lambda _: '202009')
    year_month, year, month, tmp_year_month_day, month_padded, first_week_day, month_days_num = process_year_month()
    actual = (year_month, year, month, tmp_year_month_day,
              month_padded, first_week_day, month_days_num)
    expected = ('202009', '2020', '9', '2020/9/1', '09', 1, 30)
    assert actual == expected
