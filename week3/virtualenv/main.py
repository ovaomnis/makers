

def add_one(a: int) -> int:
    return a + 1

def division(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError
    return a / b

def summa(a: int, b: int) -> int:
    return a + b

def is_palindrome(word: str) -> bool:
    return word.lower() == word.lower()[::-1]

def factorial(n: int) -> int:
    prod = 1
    for i in range(2, n + 1):
        prod = prod * i
    return prod
