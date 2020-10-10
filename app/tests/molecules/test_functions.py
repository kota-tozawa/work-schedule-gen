import pytest
from components.molecules.functions import (
    insert_string_to_base,
    separate_year_month,
    zero_padding,
    to_year_month_day,
    is_holiday,
    set_out_cell
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
    # 長さ不足
    ('202', pytest.raises(IndexError), None)
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
            assert separate_year_month(year_month) is not None
