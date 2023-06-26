string = 'Hello'

dict_ = {}
for i in string:
    print(i, string.count(i))
    dict_.update(
        {i: string.count(i)}
    )

print(dict_)

