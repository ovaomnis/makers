# square = lambda x: x**2
# print(square(2))

# a, b = list(map(int, input('Enter numbers: ').strip().split()))

# cyrillic_vowels = ['А', 'Е', 'Ё', 'И', 'Й', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
# list_ = ['Тима', "Макс", "Эртай", "Алина", "Эркаим"]
# print(list(filter(lambda name: name[0].upper() in cyrillic_vowels, list_)))

# dict_ = {1: 2, 3: 4, 5: 6}
# new_dict = dict(map(lambda x: (x, str(dict_[x])), dict_))
#
# print(new_dict)

# list_ = [1,2,3,4]
# new_list = list(map(lambda x: 'odd' if x % 2 else 'even', list_))
# print(new_list)

# print(all([True, True, True, True, True, False]))

print(hash('key'), hash('key'))
