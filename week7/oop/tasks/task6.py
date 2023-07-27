class Salary:
    percent = 8

    def __init__(self, salary: int, experience: int) -> None:
        self.salary = salary
        self.experience = experience

    def count_count_percent(self) -> float:
        return (self.percent / 100) * self.salary * self.experience


obj = Salary(10000, 10)
print(obj.count_count_percent())
