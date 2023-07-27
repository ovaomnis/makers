class A:
    def my_range(self, start, end, step):
        while start < end:
            yield start
            start += step


a1 = A()
for i in a1.my_range(1, 10, 2):
    print(i)
