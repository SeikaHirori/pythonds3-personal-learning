from recursion_sc_2 import *

def test_palindrome():

    assert (is_pal(remove_white("x")) == True)
    assert (is_pal(remove_white("radar")) == True)
    assert (is_pal(remove_white("hello")) == False)
    assert (is_pal(remove_white("")) == True)
    assert (is_pal(remove_white("hannah")) == True)
    assert (is_pal(remove_white("madam i'm adam")) == True)