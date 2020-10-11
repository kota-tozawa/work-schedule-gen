from components.atoms.constants import WEEK_DAYS
from components.molecules.exceptions import NonExistentValueError


class Date:
    def __init__(self, day: int, week_day: str, holiday_flg: bool):
        if day is None:
            raise TypeError('日付がありません。')
        if week_day is None or '':
            raise TypeError('曜日がありません。')
        if holiday_flg is None:
            raise TypeError('休日・祝日判定がありません。')

        if day < 1 or day > 31:
            raise NonExistentValueError()
        if week_day not in WEEK_DAYS:
            raise NonExistentValueError()

        self.day = day
        self.week_day = week_day
        self.holiday_flg = holiday_flg

    # getters
    @property
    def day(self) -> int:
        return self.__day

    @property
    def week_day(self) -> str:
        return self.__week_day

    @property
    def holiday_flg(self) -> bool:
        return self.__holiday_flg

    # setters
    @day.setter
    def day(self, day: int):
        self.__day = day

    @week_day.setter
    def week_day(self, week_day: str):
        self.__week_day = week_day

    @holiday_flg.setter
    def holiday_flg(self, holiday_flg: bool):
        self.__holiday_flg = holiday_flg
