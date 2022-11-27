""" 3.21.2. The UnorderedList Class
- Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementinganUnorderedListLinkedLists.html#the-unorderedlist-class
"""
from node_example import Node

class UnorderedList:
    def __init__(self) -> None:
        self.head:Node = None
        self.tail:Node = None # RFER 3
        self._count = 0
    
    def is_empty(self) -> bool:
        return self.head == None

    def add(self, item) -> None:
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

        if self.tail is None:
            self.tail = self.head

        self._count += 1

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
        
        self._count -= 1

    
    # Self-check #1 
    def append_O_n(self, item) -> None:
        if self.head == None:
            self.add(item)
            return
        
        current:Node = self.head
        previous:Node = None

        """ Use for loop to get to the last Node of list
        """
        while current is not None:
            previous = current
            current = current.next
        
        current = Node(item)
        # self.head = current # NOTE: This isn't needed I think since it fails the test when it's included in code.
        if previous is None:
            self.head = current.next
        else:
            previous.next = current

        self._count += 1

    # Self-check #2 
    def append_O_1(self, item):
        if self.head is None:
            self.head = Node(item)
            self._count += 1
        if self.tail is None: # If tail is None, loop until you get to the last Node. Assign the last Node as tail.
            current = self.head
            while current.next is not None:
                current = current.next
            self.tail = current
                
                


    def insert(self, item, pos:int=0) -> None: # TODO


        self._count += 1
        pass

    
    def index(self, item) -> int: # TODO
        pass

    def pop(self, pop:int=-1) -> Node: # TODO

        self._count -= 1
        pass

    def size(self) -> int:
        return self._count