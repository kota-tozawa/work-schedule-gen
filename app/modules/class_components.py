class Date:
    def __init__(self, date, is_holiday):
        self.date = date
        self.is_holiday = is_holiday

    def set_date(self, date):
        self.date = date

    def set_is_holiday(self, is_holiday):
        self.is_holiday = is_holiday

    def get_date(self):
        return self.date

    def get_is_holiday(self):
        return self.is_holiday
