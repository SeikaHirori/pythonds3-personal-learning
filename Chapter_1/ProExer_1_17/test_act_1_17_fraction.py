from operator import iadd
import pytest

from ProExer_1_17.act_1_17_fraction import Fraction, testRaddFraction
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

#p1
def test_getNum(): 
    #pass

    frac_getNum = Fraction(1,2)

    output_num = frac_getNum.getNum()

    assert output_num == 1, "Should return numerator: 1"



#p1
def test_getDen():
    #pass

    frac_getDen = Fraction(2,3)

    output_den = frac_getDen.getDen()

    assert output_den == 3, "Should return denominator: 3"

#p2
def test_GCD_is_used_immediately():
    f1 = Fraction(2,4)

    assert f1.getNum() == 1

    assert f1.getDen() == 2

#p2
def test_GCD_with_addition():

    f1 = Fraction(1,4)
    f2 = Fraction(1,4)

    output_gcd_a = f1 + f2

    assert output_gcd_a.getNum() == 1, "Should return Numerator: 1"
    assert output_gcd_a.getDen() == 2, "Should return Den: 2"


#p2
def test_GCD_with_subtraction():
    # pass

    f1 = Fraction(3,4)
    f2 = Fraction(1,4)

    output_gcd_sub = f1 - f2

    assert output_gcd_sub.getNum() == 1, "Should return numerator: 1"
    assert output_gcd_sub.getDen() == 2, "Should return Den: 2"

#p2
def test_GCD_with_mul():
    f1 = Fraction(1,2)
    f2 = Fraction(1,4)

    output = f1 * f2
    assert output.getNum() == 1, "Should return Numerator: 1"
    assert output.getDen() == 8, "Should return Den: 8"

#p2
def test_GCD_with_trueDiv():
    f1 = Fraction(1,3)
    f2 = Fraction(1,2)

    output = f1 / f2

    assert output.getNum() == 2, "Should return Numerator: 2"
    assert output.getDen() == 3, "Should return Den: 3"

#p4
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


#p4
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

#p4
def test__ne__(): 
    f1 = Fraction(1,2)
    f2 = Fraction(2,3)

    assert (f1 != f2) == True, "Should return: True"


    f3 = Fraction(1,2)
    f4 = Fraction(1,2)

    assert (f3 != f4) == False, "Should return: False"

#p5
def test_constructor_check_num_valid_integers(capsys):

    with pytest.raises(SystemExit):
        f1 = Fraction("beep",2)
    captured = capsys.readouterr()
    assert captured.out == 'beep is not an integer!\n'
    
#p5
def test_constructor_check_den_valid(capsys):

    with pytest.raises(SystemExit) as e_info: # Now checking for 
        f1 = Fraction(2, "meeeeeep")
    captured = capsys.readouterr()
    assert captured.out == 'meeeeeep is not an integer!\n'

    f2 = Fraction(1,2)

    assert f2.getNum() == 1, "Should return Num: 1"
    assert f2.getDen() == 2, "Should return Den: 2"


#p6
def test_negative_denominator():
    f1 = Fraction(1,-5)

    assert f1.getDen() == 5, "Den should return 5"
    assert f1.getNum() == -1, "Num should return -1"

#p7
def test__radd__(): # this test... doesn't fail. Not sure how to test for __radd__.
        #UPDATE: made a separate class that only had num and den; no other functions were there.
            #Reference SOF: https://stackoverflow.com/a/38196153
    f1 = Fraction(1,2)
    f2 = testRaddFraction(1,4)
    
    sum_f1_first = f1 + f2
    sum_f1_second = f2 + f1

    assert sum_f1_first.getNum() == 3
    assert sum_f1_first.getDen() == 4

    assert sum_f1_second.getNum() == 3
    assert sum_f1_second.getDen() == 4

#p8
def test__iadd__(): # wrote this test, and it did not fail. Not sure how to test for "+="/__iadd__
    foo = Fraction(1,2)
    bar = Fraction(1,4)

    combined = iadd(foo,bar)

    assert combined.getNum() == 3
    assert combined.getDen() == 4

    foo += bar

    assert foo.getNum() == 3
    assert foo.getDen() == 4

    