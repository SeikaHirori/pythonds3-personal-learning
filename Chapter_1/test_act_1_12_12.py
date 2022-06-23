import pytest

from act_1_12_1 import code

# Activity link: https://runestone.academy/ns/books/published/pythonds3/Introduction/DefiningFunctions.html

class test_code:
    def __init__(self):
        self.code_class = code()
    
    def test_hello():
        testCode = code()
        assert testCode.get_hello() == 'Hello'