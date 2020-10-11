import pytest
from components.processes.process_name import process_name


@pytest.mark.integtest
def test_process_name(monkeypatch):
    # 正常
    monkeypatch.setattr('builtins.input', lambda _: '氏名')
    monkeypatch.setattr(
        'components.organisms.get_name.get_last_or_first_name', lambda _: '氏名')
    last_name, first_name, full_name = process_name()
    actual = (last_name, first_name, full_name)
    expected = ('氏名', '氏名', '氏名氏名')
    assert actual == expected
