import pytest
from components.organisms.get_holiday_list import get_holiday_list


@pytest.mark.integtest
def test_get_holiday_list():
    # 正常
    assert get_holiday_list(31, 5, '2017', '07') is not None
    assert get_holiday_list(31, 3, '2020', '10') is not None
