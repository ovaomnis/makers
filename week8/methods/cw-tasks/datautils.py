class DataUtils:
    @classmethod
    def is_valid_date(cls, date: str) -> bool:
        import datetime
        year, month, day = map(int, date.split('-'))
        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False


print(DataUtils.is_valid_date('2022-12-2'))
