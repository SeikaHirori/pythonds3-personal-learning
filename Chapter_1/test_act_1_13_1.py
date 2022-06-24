from act_1_13_1 import Fraction

# Link to URL: https://runestone.academy/ns/books/published/pythonds3/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html #a-fraction-class

def test_show(capsys):
    testFrac = Fraction(3,5)

    testFrac.show()
    captured = capsys.readouterr()

    assert captured.out == "3/5\n"

def test__str___By_printing(capsys):
    testFrac = Fraction(1,6)

    print(testFrac)
    captured = capsys.readouterr()

    assert captured.out == "1/6\n", 'Should return 1/6\n'

def test__str___byDirectlyCalling():
    testFrac = Fraction(10,11)



    assert testFrac.__str__ == 10/11

    assert str(testFrac) == '10/11'