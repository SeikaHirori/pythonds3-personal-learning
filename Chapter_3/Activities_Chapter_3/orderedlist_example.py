""" 3.23. Implementing an Ordered List¶
    - Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementinganOrderedList.html
"""
from node_example import Node

class OrderList:
    def __init__(self) -> None: # TODO
        self._head:Node = None
        self._tail:Node = None
        self._count:int = 0
    
    def add(self, item) -> None: # TODO
        new_item:Node = Node(item)
        current = self._head
        previous = None

        while current is not None and current.data < item:
            previous = current
            current = current.next
        
        if previous is None:
            new_item.next = self._head
            self._head = new_item
        else:
            new_item.next = current
            previous.next = new_item
        
        if self._tail is None:
            self._tail = new_item
        elif self._tail.data < new_item.data:
            self._tail = new_item
        
        self._count += 1


    def remove(self, item) -> None: # TODO
        pass

    def search(self, item) -> bool: # TODO
        current:Node = self._head
        while current is not None:
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next
        
        return False

    def is_empty(self) -> bool: # TODO
        return self._count == 0

    def size(self) -> int: # TODO
        return self._count

    def index(self, item) -> int: # TODO
        output = 0
        temp:Node = Node(item)

        current:Node = self._head
        
        while current is not None:
            output += 1

            if current.data > temp.data:
                return -1
            if current.data == temp.data:
                return output - 1
            current = current.next

        return -1

    def pop(self, pos=-1) -> Node: # TODO
        pass

    def debug_all_node_values(self) -> list:
        output:list = []
        if self._count == 0:
            return []

        current = self._head
        while current is not None:
            output.append(current.data)
            current = current.next

        return output