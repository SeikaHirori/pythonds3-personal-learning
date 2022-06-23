import pytest

from act_1_12_1 import code

# Activity link: https://runestone.academy/ns/books/published/pythonds3/Introduction/DefiningFunctions.html


    
def test_hello():
    testCode = code()
    assert testCode.get_hello() == 'Hello'