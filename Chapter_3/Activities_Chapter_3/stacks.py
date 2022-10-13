"""
Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementingaStackinPython.html#lst-stackcode1

"""

class Stack:
    def __init__(self) -> None:
        self._items:list = []

    def is_empty(self) -> bool:

        # Returns True if empty; False is there's anything in the list
        return not bool(self._items) 
    
    def push(self, item) -> None:
        return self._items.append(item)

    def pop(self):
        return self._items.pop()
    
    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)