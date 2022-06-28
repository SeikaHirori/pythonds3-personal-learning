import pytest

from ProExer_1_17.act_1_17_fraction import Fraction
    # Importing a file/class from another folder: https://stackoverflow.com/a/456491
        # Create a blank "__init__.py" file to do this.

#misc
def test__gt__with_refactored_function():
    f1 = Fraction(1,2)
    f2 = Fraction(1,100)

    output = (f1 > f2)
    assert output == True

def test_getDecimalVersion():
    frac = Fraction(1,2)

    assert frac.getDecimalVersion() == .5, "Should return: .5"

#1
def test_getNum(): 
    #pass

    frac_getNum = Fraction(1,2)

    output_num = frac_getNum.getNum()

    assert output_num == 1, "Should return numerator: 1"



#1
def test_getDen():
    #pass

    frac_getDen = Fraction(2,3)

    output_den = frac_getDen.getDen()

    assert output_den == 3, "Should return denominator: 3"

#2
def test_GCD_is_used_immediately():
    f1 = Fraction(2,4)

    assert f1.getNum() == 1

    assert f1.getDen() == 2

#2
def test_GCD_with_addition():

    f1 = Fraction(1,4)
    f2 = Fraction(1,4)

    output_gcd_a = f1 + f2

    assert output_gcd_a.getNum() == 1, "Should return Numerator: 1"
    assert output_gcd_a.getDen() == 2, "Should return Den: 2"


#2
def test_GCD_with_subtraction():
    # pass

    f1 = Fraction(3,4)
    f2 = Fraction(1,4)

    output_gcd_sub = f1 - f2

    assert output_gcd_sub.getNum() == 1, "Should return numerator: 1"
    assert output_gcd_sub.getDen() == 2, "Should return Den: 2"

#2
def test_GCD_with_mul():
    f1 = Fraction(1,2)
    f2 = Fraction(1,4)

    output = f1 * f2
    assert output.getNum() == 1, "Should return Numerator: 1"
    assert output.getDen() == 8, "Should return Den: 8"

#2
def test_GCD_with_trueDiv():
    f1 = Fraction(1,3)
    f2 = Fraction(1,2)

    output = f1 / f2

    assert output.getNum() == 2, "Should return Numerator: 2"
    assert output.getDen() == 3, "Should return Den: 3"

#4
def test__ge__():
    f1 = Fraction(1,4)
    f2 = Fraction(1,5)

    result_ge_true_f1 = (f1 >= f2)

    assert result_ge_true_f1 == True, "Should return: True"

    f3 = Fraction(1,5)
    f4 = Fraction(1,5)

    result_ge_true_equals = (f3 >= f4)

    assert result_ge_true_equals == True

    f5 = Fraction(1,6)
    f6 = Fraction(1,5)

    result__ge__false = (f5 >= f6)

    assert result__ge__false == False, "Should return: False"


#4
def test__le__(): 
    f1 = Fraction(1,5)
    f2 = Fraction(1,3)
    output_true_less = (f1 <= f2)

    assert output_true_less == True, "Should return: True"


    f3 = Fraction(1,5)
    f4 = Fraction(1,5)
    output_true_equals = (f3 <= f4)

    assert output_true_equals == True, "Should return: True"


    f5 = Fraction(1,2)
    f6 = Fraction(1,5)
    output_false = (f5 <= f6)
    
    assert output_false == False, "Should return: False"

#4
def test__ne__(): 
    f1 = Fraction(1,2)
    f2 = Fraction(2,3)

    assert (f1 != f2) == True, "Should return: True"


    f3 = Fraction(1,2)
    f4 = Fraction(1,2)

    assert (f3 != f4) == False, "Should return: False"

#TODO
#5
def test_constructor_check_num_valid_integers():
    
    with pytest.raises(Exception) as e_info:
        f1 = Fraction("beep", 2)
    
#TODO
#5
def test_constructor_check_den_valid():

    with pytest.raises(Exception) as e_info:
        f1 = Fraction(2, "meeeeeep")


    

    

