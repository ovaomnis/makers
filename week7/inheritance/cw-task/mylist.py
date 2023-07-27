class MyList(list):
    def insert(self, __object, __index) -> None:
        super().insert(__index, __object)


mylist = MyList([1, 2, 3, 4, 5])
mylist.insert('Hello', 0)
print(mylist)
