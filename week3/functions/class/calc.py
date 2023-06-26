from functions import my_len

def summa(a, b):
    return a + b

def substruct(a, b):
    return a - b

def multiply(a, b):
    return a*b

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Second num is zero')

def power(a, b):
    return a**b

def module(a, b):
    return a%b

operators = {
    '+': summa,
    '-': substruct,
    '*': multiply,
    '/': divide,
    '**': power,
    '%': module
}

while True:
    a, b, oper = int(input('enter first number: ')), int(input('enter second number: ')), input('choose operator "+ - * / ** %": ')
    print()
    if oper in operators:
        print(operators[oper](a, b))
    else:
        print('no such operator')
    
    if input('Do You wanna continue (y/n): ') != 'y':
        break
