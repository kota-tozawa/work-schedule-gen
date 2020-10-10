import pytest
from components.molecules.classes import Date


class TestDate:
    def test_get_day_normal(self):
        assert Date(9, '月', False).day == 9

    def test_get_day_negative(self):
        assert Date(-1, '月', False).day == 0

    def test_get_day_none(self):
        with pytest.raises(TypeError):
            assert Date(None, '月', False)

    def test_get_week_day_normal(self):
        assert Date(18, '水', False).week_day == '水'

    def test_get_week_day_none(self):
        with pytest.raises(TypeError):
            assert Date(18, None, False).week_day

    def test_get_holiday_flg_normal(self):
        assert Date(20, '木', True).holiday_flg == True

    def test_get_holiday_flg_none(self):
        with pytest.raises(TypeError):
            Date(20, '木', None).holiday_flg
