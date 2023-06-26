dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
dict2 = {k: list(v.values())[0] for k, v in dict_.items()}
print(dict2)