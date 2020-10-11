import pytest
from components.organisms.get_year_month import get_year_month


@pytest.mark.integtest
def test_get_year_month(monkeypatch):
    # 正常（6桁）
    monkeypatch.setattr('builtins.input', lambda _: '202009')
    actual = get_year_month()
    expected = '202009'
    assert actual == expected

    # 正常（5桁）
    monkeypatch.setattr('builtins.input', lambda _: '20209')
    actual = get_year_month()
    expected = '202009'
    assert actual == expected
