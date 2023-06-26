'''Functions'''

'''Annotation which helps to make code more intel and helps to fix dynamic typing issue'''

# num: int = 10 #alerting that there is only integer type
# num = 'hello'
# print(num)

'''================================== Functions =================================='''
# functions is named code block, which dispatches some sort of function
# able to take arguemtns and returns result
# functions can be used many times

# to define funtion we use 'def' keyword and then we give name of this function
# def <func_name>(args):
#     <body>
#     ?return

def my_len(obj: list[int]): return len(obj)

print(my_len([1,2,3,4]))

# return -> operator which says to return function result, without retunr function will return None

''' Argument Types '''

# 1. required arguements
# def func(a, b, c):
#     pass

# 2. non required args
# def func(a = 1, b = None):
#     pass


# def func(a, *args, **kwargs):
#     print(a)
#     print(args)
#     print(kwargs)

# func(1, 'hello', 'world', name = 'adil')