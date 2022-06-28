import pytest

from ProExer_1_17.act_1_17_fraction import Fraction
    # Importing a file/class from another folder: https://stackoverflow.com/a/456491
        # Create a blank "__init__.py" file to do this.

#TODO
#1
def test_getNum(): 
    #pass

    frac_getNum = Fraction(1,2)

    output_num = frac_getNum.getNum()

    assert output_num == 1, "Should return numerator: 1"



#TODO
#1
def test_getDen():
    #pass

    frac_getDen = Fraction(2,3)

    output_den = frac_getDen.getDen()

    assert output_den == 3, "Should return denominator: 3"

#TODO
#3
def test__ge__():
    f1 = Fraction(1,5)
    f2 = Fraction(1,4)

    result_ge_true_f1 = (f1 >= f2)

    assert result_ge_true_f1 == True, "Should return: True"

    f3 = Fraction(1,5)
    f4 = Fraction(1,5)

    result_ge_true_equals = (f3 >= f4)

    assert result_ge_true_equals == True


#TODO
#3
def test__le__(): 
    pass

#TODO
#3
def test__ne__(): 
    pass

#TODO
#4
def test_constructor_checks_valid_integers():
    pass