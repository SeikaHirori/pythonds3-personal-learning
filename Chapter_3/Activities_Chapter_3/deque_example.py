

class Deque:
    def __init__(self) -> None:
        self._items:list = []
    
    def add_front(self, item):
        self._items.insert(0, item)

    def add_rear(self, item):
        self._items.append(item)

    def remove_front(self):
        return self._items.pop(0)

    def remove_rear(self):
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
    
    def peek_list(self):
        return self._items