class Date:
    def __init__(self, day: int, week_day: str, holiday_flg: bool):
        self.day = day if day > 0 else 0
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
        if day is None:
            raise TypeError('不正な日付です。')
        self.__day = day

    @week_day.setter
    def week_day(self, week_day: str):
        if week_day is None or '':
            raise TypeError('不正な曜日です。')
        self.__week_day = week_day

    @holiday_flg.setter
    def holiday_flg(self, holiday_flg: bool):
        if holiday_flg is None:
            raise TypeError('不正な休日・祝日判定です。')
        self.__holiday_flg = holiday_flg
