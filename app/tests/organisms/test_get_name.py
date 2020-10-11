import pytest
from components.organisms.get_name import get_last_or_first_name


@pytest.mark.integtest
def test_get_last_or_first_name(monkeypatch):
    # 正常（苗字）
    monkeypatch.setattr('builtins.input', lambda _: '範馬')
    actual = get_last_or_first_name()
    expected = '範馬'
    assert actual == expected

    # 正常（名前）
    monkeypatch.setattr('builtins.input', lambda _: '勇次郎')
    actual = get_last_or_first_name(last_name=False)
    expected = '勇次郎'
    assert actual == expected
