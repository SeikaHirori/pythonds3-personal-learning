""" 3.18. Palindrome Checker¶
- Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/PalindromeChecker.html
"""
from pythonds3.basic import Deque

def pal_checker(a_string:str) -> bool:
    char_deque = Deque()

    for character in a_string:
        char_deque.add_rear(character)
    
    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()

        if first != last:
            return False
        
    return True
