""" 3.6. Simple Balanced Parentheses
Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/SimpleBalancedParentheses.html
"""

from stacks import Stack
class par_checker:
    def par_checker(self, symbol_string:str):
        stack = Stack()
        
        for symbol in symbol_string:
            if symbol == "(":
                stack.push(symbol)
            else:
                if stack.is_empty():
                    return False
                else:
                    stack.pop()

        return stack.is_empty()