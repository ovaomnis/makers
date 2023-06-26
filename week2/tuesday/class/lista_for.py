''' List - data type'''
# mutable, ordered, indexable, iterable data type

# [] -> literal (expression or constant which creates object)
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, [True, "hello"], 'hello', {'key': 'value'}, (1, 2, )]
# print(list_[0])
# print(list_[9][0])
# print(list_[-1])

# print(id(list_))
# list_[0] = 'hello'
# print(id(list_))


'============================ Creating Lists ============================'
# 1. list(iterable)
# list_1 = list('hello world')
# print(list_1)

# 2. []
# a = [1, 2, 3, 4, 5, 6]
# print(type(a))

# 3. range(start, end - 1, step) => returns sequence of element from start to end
# list_2 = list(range(1, 11))
# print(list_2)
# range(start, end, step)
# end => till the end
# start => from where to start
# step

'============================ List methods ============================'
# list.append(element) => adds element to the end of list

# list_3 = [1, 2, 3, 'hello', 'world', 'test']
# list_3.append(5)
# print(list_3)
# list_3.append([1, 2, 3, 4])
# print(list_3)

# list.extend(iter)

# list_4 = [1, 2, 3, 4, 5]
# list_4.extend(['hello', 'world'])
# print(list_4)

# list.insert(index, element)
# list.index(element, [start, end])



