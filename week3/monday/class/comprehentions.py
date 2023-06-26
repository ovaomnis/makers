'''====================== Comprehenstions ======================'''
# generation some sort of list, dict, set

# List comprehentions
# list_ = [i**2 if i%2 else i**3 for i in range(1, 50) if not i%4]
# print(list_)

# Dict comprehentions
# dict1 = {
#     'Vasya': {
#         'likes': 12,
#         'friends': 999
#     },
#     'Kolya': {
#         'likes': 12,
#         'friends': 999
#     },
#     'Sasha': {
#         'likes': 12,
#         'friends': 999
#     },
#     'Gena': {
#         'likes': 12,
#         'friends': 999
#     },
#     'Reyna': {
#         'likes': 12,
#         'friends': 999
#     }
# }

# dict2 = [f'{name} has {value} {key}' for name, meta in dict1.items() for key, value in meta.items()]
# print('\n'.join(dict2))

# dict_ = {i: i**2 for i in range(1, 11)}
# print(dict_)

# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']

# dict1 = {i: list2[i-1] if i <= len(list2) else None for i in list1}
# print(dict1)