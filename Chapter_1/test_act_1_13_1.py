from termios import FF1
from act_1_13_1 import Fraction

# Link to URL: https://runestone.academy/ns/books/published/pythonds3/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html #a-fraction-class

def test_show(capsys):
    testFrac = Fraction(3,5)

    testFrac.show()
    captured = capsys.readouterr()

    assert captured.out == "3/5\n"

def test__str___by_printing(capsys):
    testFrac = Fraction(1,6)

    print(testFrac)
    captured = capsys.readouterr()
    assert captured.out == "1/6\n", 'Should return 1/6\n'

    print(testFrac.__str__())
    captured = capsys.readouterr()
    assert captured.out == "1/6\n", 'Should return 1/6\n'

    print(str(testFrac))
    captured = capsys.readouterr()
    assert captured.out == "1/6\n", 'Should return 1/6\n'

# def test__add__raw(capsys): # Depreciated
    
#     f1 = Fraction(3,10)
#     f2 = Fraction(2,5)

#     f3 = f1 + f2
#     print(f3)
#     captured = capsys.readouterr()
#     assert captured.out == '35/50\n', 'Should return 35/50\n'


def test_gcd(capsys): 
    # Doc about static method and to obtain output: https://python-course.eu/oop/class-instance-attributes.php
        # Section: Static Methods
    
    f1 = Fraction(35,50)

    print(f1.gcd(20, 10))

    captured = capsys.readouterr()

    assert captured.out == '10\n'

def test_simplified_sum(capsys):
    f1 = Fraction(3,10)
    f2 = Fraction(2,5)

    f3 = f1 + f2

    print(f3)
    captured = capsys.readouterr()
    assert captured.out == '7/10\n', 'Should return "7/10\n"'

def test___eq__():
    f1 = Fraction(1,2)
    f2 = Fraction(1,2)

    assert (f1 == f2) == True, 'Should return True'

    f3 = Fraction(400, 6000)
    f4 = Fraction(900, 9999999)

    assert (f3 == f4) == False,'Should return False'

