def type_check(correct_type):
    def decorator(func):
        def wrapper(arg):
            if type(arg) == correct_type:
                func(arg)
            else:
                print('Неверный тип данных :(')
        return wrapper
    return decorator


@type_check(int)
def func1(num):
    print(num**2)


func1(2)
func1({1: 'какой-то', 2: 'словарь'})

