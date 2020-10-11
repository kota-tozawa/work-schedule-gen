import pytest
from components.molecules.exceptions import (
    TooLongStringError,
    TooShortStringError,
)
from components.molecules.functions import (
    insert_string_to_base,
    separate_year_month,
    zero_padding,
    to_year_month_day,
    is_holiday,
)


# テストデータ
insert_string_to_base_data = [
    # 正常
    ('ABCFG', 3, 'DE', 'ABCDEFG'),
    # 挿入対象文字列の長さの範囲外のinsert_point
    ('ABCDEF', 100, 'X', 'ABCDEFX'),
    ('ABCDEF', -100, 'X', 'XABCDEF'),
]

separate_year_month_data = [
    # 正常
    ('202009', '2020', '9'),
    ('20209', '2020', '9'),
    ('198411', '1984', '11'),
    # 長さ4文字以下
    ('202', pytest.raises(IndexError), None),
    # 長さ6文字以上
    ('7777777', pytest.raises(TooLongStringError), None),
]

zero_padding_data = [
    # 正常
    ('7', '07'),
    ('19', '19'),
    # 長さ0文字
    ('', ''),
    # 長さ3文字以上
    ('333', pytest.raises(TooLongStringError)),
]

to_year_month_day_data = [
    # 正常
    ('2020', '09', '01', '20200901'),
    # 長さ不足
    ('202', '09', '01', pytest.raises(TooShortStringError)),
    ('2020', '9', '01', pytest.raises(TooShortStringError)),
    ('2020', '09', '1', pytest.raises(TooShortStringError)),
    # 長さオーバー
    ('20201', '09', '01', pytest.raises(TooLongStringError)),
    ('2020', '111', '01', pytest.raises(TooLongStringError)),
    ('2020', '09', '111', pytest.raises(TooLongStringError)),
]

is_holiday_data = [
    # 正常
    ('20200901', False),  # 平日
    ('20200919', True),  # 休日
    ('20200921', True),  # 祝日（敬老の日）
    # 長さ7文字以下
    ('2020091', pytest.raises(TooShortStringError)),
    # 長さ9文字以上
    ('202009011', pytest.raises(TooLongStringError)),
]


# テスト
@pytest.mark.parametrize(('base_string', 'insert_point', 'insert_string', 'expected'), insert_string_to_base_data)
def test_insert_string_to_base(base_string, insert_point, insert_string, expected):
    assert insert_string_to_base(
        base_string, insert_point, insert_string) == expected


@pytest.mark.parametrize(('year_month', 'expected1', 'expected2'), separate_year_month_data)
def test_separate_year_month(year_month, expected1, expected2):
    try:
        separate_year_month(year_month)
        assert separate_year_month(year_month) == (expected1, expected2)
    except IndexError:
        with expected1:
            assert separate_year_month(year_month)
    except TooLongStringError:
        with expected1:
            assert separate_year_month(year_month)


@pytest.mark.parametrize(('value', 'expected'), zero_padding_data)
def test_zero_pading(value, expected):
    try:
        zero_padding(value)
        assert zero_padding(value) == expected
    except TooLongStringError:
        with expected:
            assert zero_padding(value)


@pytest.mark.parametrize(('year', 'month_padded', 'day_padded', 'expected'), to_year_month_day_data)
def test_to_year_month_day(year, month_padded, day_padded, expected):
    try:
        to_year_month_day(year, month_padded, day_padded)
        assert to_year_month_day(year, month_padded, day_padded) == expected
    except TooShortStringError:
        with expected:
            assert to_year_month_day(
                year, month_padded, day_padded)
    except TooLongStringError:
        with expected:
            assert to_year_month_day(
                year, month_padded, day_padded)


@pytest.mark.parametrize(('str_date', 'expected'), is_holiday_data)
def test_is_holiday(str_date, expected):
    try:
        is_holiday(str_date)
        assert is_holiday(str_date) == expected
    except TooShortStringError:
        with expected:
            assert is_holiday(str_date)
    except TooLongStringError:
        with expected:
            assert is_holiday(str_date)
