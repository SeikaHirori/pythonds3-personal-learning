""" 3.7. Balanced Symbols (A General Case)¶

Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/BalancedSymbolsAGeneralCase.html
"""
from stacks import Stack

class balance_checker:
    def balance_checker(self, symbol_string):
        s = Stack()
        for symbol in symbol_string:
            if symbol in "([{":
                s.push(symbol)
            else:
                if s.is_empty():
                    return False
                else:
                    if not self.matches(s.pop(), symbol):
                        return False
        return s.is_empty()

    def matches(self, sym_left, sym_right):
        all_lefts:str = "([{"
        all_rights:str = "}])"

        return all_lefts.index(sym_left) == all_rights.index(sym_right)