import pytest
from components.molecules.classes import Date


class TestDate:
    def test_get_day_normal():
        assert Date(9, '月', False).day == 9

    def test_get_day_negative():
        assert Date(-1, '月', False).day == 0

    def test_get_day_none():
        with pytest.raises(TypeError('不正な日付です。')):
            assert Date(None, '月', False)

    def test_get_week_day_normal():
        assert Date(18, '水', False).week_day == '月'

    def test_get_week_day_none():
        with pytest.raises(TypeError('不正な曜日です。')):
            assert Date(18, None, False).week_day

    def test_get_holiday_flg_normal():
        assert Date(20, '木', True).holiday_flg == True

    def test_get_holiday_flg_none():
        with pytest.raises(TypeError('不正な休日・祝日判定です。')):
            Date(20, '木', None).holiday_flg
