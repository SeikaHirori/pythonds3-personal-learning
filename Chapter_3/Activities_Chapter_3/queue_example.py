

class Queue_example:
    def __init__(self) -> None:
        self._items = []
    
    def is_empty(self) -> bool:
        return not self._items

    def size(self) -> int:
        return len(self._items)

    def enqueue(self, value) -> None:
        self._items.append(value)
    
    def dequeue(self):
        return self._items.pop(0)