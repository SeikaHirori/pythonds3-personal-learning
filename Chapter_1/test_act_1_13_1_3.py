import pytest

from act_1_13_1_3 import Fraction

# URL: https://runestone.academy/ns/books/published/pythonds3/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html#lst-fractioncode

def test__mul__(capsys): # Multiplication
    f1 = Fraction(3,5)
    f2 = Fraction(1,2)

    f3 = f1 * f2
    print(f3)
    captured = capsys.readouterr()

    assert captured.out == '3/10\n', 'Should return: 3/10\n'

def test__truediv__(capsys): # Division
    f1 = Fraction(1,5)
    f2 = Fraction(2,7)
    
    f3 = f1 / f2
    print(f3)
    captured = capsys.readouterr()

    assert captured.out == '7/10\n', 'Should return: 7/10\n'

def test__sub__(capsys): # Subtraction
    f1 = Fraction(2, 5)
    f2 = Fraction(2, 6)

    f3 = f1 - f2
        # '24/30' before simplifying
        # '4/5' afterwards
    print(f3)
    captured = capsys.readouterr()

    assert captured == '4/5\n', 'Should return: 4/5\n'

def test__lt__(): # Less Than | a < b
    # False result
    f1 = Fraction(3, 10)
    f2 = Fraction(1, 10)

    f3 = f1 < f2

    assert f3 == False, 'Should return: False'

    # True result
    w1 = Fraction(1, 19)
    w2 = Fraction(1, 2)

    w3 = w1 < w2

    assert w3 == True,' Should return: True'

def test__gt__(): # Greater than | a > b
    # False result
    f1 = Fraction(1, 10)
    f2 = Fraction(7, 10)
    
    f3 = f1 > f2

    assert f3 == False

    # True result
    w1 = Fraction(33, 34)
    w2 = Fraction(1, 10)

    w3 = w1 > w2

    assert w3 == True