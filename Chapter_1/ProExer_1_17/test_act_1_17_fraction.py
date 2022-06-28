import pytest

from ProExer_1_17.act_1_17_fraction import Fraction
    # Importing a file/class from another folder: https://stackoverflow.com/a/456491
        # Create a blank "__init__.py" file to do this.

def test__ge__():
    f1 = Fraction(1,5)
    f2 = Fraction(1,4)

    result_ge_true_f1 = (f1 >= f2)

    assert result_ge_true_f1 == True, "Should return: True"

    f3 = Fraction(1,5)
    f4 = Fraction(1,5)

    result_ge_true_equals = (f3 >= f4)

    assert result_ge_true_equals == True