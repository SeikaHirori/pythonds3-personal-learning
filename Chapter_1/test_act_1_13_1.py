from act_1_13_1 import Fraction



def test_show(capsys):
    testFrac = Fraction(3,5)

    testFrac.show()
    captured = capsys.readouterr()

    assert captured.out == "3/5\n"