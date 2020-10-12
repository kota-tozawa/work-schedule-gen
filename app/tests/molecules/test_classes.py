import pytest
from components.molecules.classes import Date
from components.molecules.exceptions import NonExistentValueError


class TestDate:
    # Test day
    def test_day_normal(self):
        assert Date(9, '月', False).day == 9

    def test_day_negative(self):
        with pytest.raises(NonExistentValueError):
            assert Date(-1, '月', False)

    def test_day_none(self):
        with pytest.raises(TypeError):
            assert Date(None, '月', False)

    def test_day_nonexistent(self):
        with pytest.raises(NonExistentValueError):
            assert Date(32, '月', False)

    # Test week_day
    def test_week_day_normal(self):
        assert Date(18, '水', False).week_day == '水'

    def test_week_day_none(self):
        with pytest.raises(TypeError):
            assert Date(18, None, False).week_day

    def test_week_day_nonexistent(self):
        with pytest.raises(NonExistentValueError):
            assert Date(18, 'あ', False)

    # Test holiday_flg
    def test_holiday_flg_normal(self):
        assert Date(20, '木', True).holiday_flg is True

    def test_holiday_flg_none(self):
        with pytest.raises(TypeError):
            Date(20, '木', None).holiday_flg

    # No args at all
    def test_date_no_args(self):
        with pytest.raises(TypeError):
            assert Date()

    # Only day
    def test_date_only_day(self):
        with pytest.raises(TypeError):
            assert Date(1)

    # Only week_day
    def test_date_only_week_day(self):
        with pytest.raises(TypeError):
            assert Date('金')

    # Only holiday_flg
    def test_date_only_holiday_flg(self):
        with pytest.raises(TypeError):
            assert Date(True)

    # w/o day
    def test_date_without_day(self):
        with pytest.raises(TypeError):
            assert Date('土', True)

    # w/o week_day
    def test_date_without_week_day(self):
        with pytest.raises(TypeError):
            assert Date(1, False)

    # w/o holiday_flg
    def test_date_without_holiday_flg(self):
        with pytest.raises(TypeError):
            assert Date(1, '日')
