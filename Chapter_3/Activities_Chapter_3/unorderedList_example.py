""" 3.21.2. The UnorderedList Class
- Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementinganUnorderedListLinkedLists.html#the-unorderedlist-class
"""
from node_example import Node

class UnorderedList:
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self) -> bool:
        return self.head == None

    def add(self, item) -> None:
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self) -> int:
        current = self.head
        count:int = 0

        while current is not None:
            print(current)
            print(f'Next: {current.next}')
            print()
            count = count + 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False
    
    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next
        
        if current is None:
            raise ValueError(f"{item} is not in the list")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next