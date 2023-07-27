class Math:
    def __init__(self, number: int):
        self.number = number

    def get_factorial(self):
        res = 1
        for i in range(1, self.number+1):
            res *= i
        return res

    def get_sum(self):
        return sum([int(i) for i in str(self.number)])

    def get_mul_table(self):
        return '\n'.join([f'{self.number}x{i}={self.number * i}' for i in range(1, 11)])


math = Math(11)

print(math.get_factorial())
print(math.get_sum())
print(math.get_mul_table())