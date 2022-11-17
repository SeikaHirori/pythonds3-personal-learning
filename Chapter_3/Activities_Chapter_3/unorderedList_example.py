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
        
        

        return False