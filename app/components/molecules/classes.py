class Date:
    def __init__(self, day, week_day, holiday_flg):
        self.day = day if day > 0 else 0
        self.week_day = week_day
        self.holiday_flg = holiday_flg

    # getters
    @property
    def day(self):
        return self.__day

    @property
    def week_day(self):
        return self.__week_day

    @property
    def holiday_flg(self):
        return self.__holiday_flg

    # setters
    @day.setter
    def day(self, day):
        if day is None:
            raise TypeError('不正な日付です。')
        self.__day = day

    @week_day.setter
    def week_day(self, week_day):
        if week_day is None:
            raise TypeError('不正な曜日です。')
        self.__week_day = week_day

    @holiday_flg.setter
    def holiday_flg(self, holiday_flg):
        if holiday_flg is None:
            raise TypeError('不正な休日・祝日判定です。')
        self.__holiday_flg = holiday_flg
