class Date:
    def __init__(self, day, week_day, holiday_flg):
        self.day = day
        self.week_day = week_day
        self.holiday_flg = holiday_flg

    def set_day(self, day):
        self.day = day

    def set_week_day(self, week_day):
        self.week_day = week_day

    def set_holiday_flg(self, holiday_flg):
        self.holiday_flg = holiday_flg

    def get_day(self):
        return self.day

    def get_week_day(self):
        return self.week_day

    def get_holiday_flg(self):
        return self.holiday_flg
