""" 3.18. Palindrome Checker¶
- Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/PalindromeChecker.html
"""

from palindrome_checker import *

def test_palindrome_checler():

    a_string:str = "lsdkjfskf"
    assert pal_checker(a_string=a_string) == False

    a_string = "radar"
    assert pal_checker(a_string=a_string) == True