import calendar
from datetime import datetime
from abc import ABC, abstractmethod


class DayAndDates(ABC):
    format = "%Y/%m/%d"

    @abstractmethod
    def define_days(self):
        """defines days"""
        pass

    @abstractmethod
    def define_date(self):
        """defines dage"""
        pass


class Current(DayAndDates):
    def define_date(self):
        return f'Current date is: {datetime.now().strftime(self.format)}'

    def define_days(self):
        ...


class MonthStart(DayAndDates):
    def define_date(self):
        curr_date = datetime.now()
        first_day_date = curr_date.replace(day=1)
        return f'First day of this week: {first_day_date.strftime(self.format)}, Amount of day from first till today: {(curr_date - first_day_date).days}'

    def define_days(self):
        ...


class MonthEnd(DayAndDates):
    def define_date(self):
        curr_date = datetime.now()
        last_day = calendar.monthrange(curr_date.year, curr_date.month)[-1]
        return f'Last day of this month is: {last_day}. Till last day left: {abs(last_day - curr_date.day)}'

    def define_days(self):
        pass


current = Current()
print(current.define_date())
month_start = MonthStart()
print(month_start.define_date())
month_end = MonthEnd()
print(month_end.define_date())
