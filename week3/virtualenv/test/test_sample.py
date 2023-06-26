from main import add_one, division, summa, is_palindrome, factorial
import pytest

def test_answer():
    assert add_one(5) == 6
    assert add_one(9) == 10
    assert add_one(15) == 16
    assert add_one(3) == 4
    assert add_one(2) == 3

def test_div():
    assert division(4, 2) == 2.0

def test_division2():
    with pytest.raises(ZeroDivisionError):
        division(2, 0)

def test_sum():
    t = [(1,2,3), (2,5,7), (5,4,9)]
    for i in t:
        assert summa(i[0], i[1]) == i[2]

def test_palindrome():
    assert is_palindrome('довод') == True

def test_fac():
    assert factorial(5) == 120