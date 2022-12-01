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
            self.tail = temp

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
        new_node:Node = Node(item)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if self.tail is None: # If tail is None, loop until you get to the last Node. Assign the last Node as tail.
                current = self.head
                while current.next is not None:
                    current = current.next
                self.tail = current
            
            self.tail.set_next(new_node)
            self.tail = new_node
        
        self._count += 1

                
                


    def insert(self, item, pos:int=0) -> None: # TODO


        self._count += 1
        pass

    
    def index(self, item) -> int: 
        if self.head is None:
            return

        output:int = None
        
        current = self.head
        index = 0
        while current is not None:
            if current.get_data() == item:
                output = index
                break
            current = current.next
            index += 1

        return output

    def pop(self, index_pop:int=-1) -> Node: # TODO
        # The value from index_pop should be based on index starting at 0 for the first element
        # Default value for index_pop is last variable

        if index_pop > self.size() - 1:
            print(f"Value of index_pop ({index_pop}) exceeded the amount of items stored in linked list.")
            return
        elif index_pop <= -1:
            while index_pop < 0:
                index_pop += self.size()
        # else: #NOTE: THIS IS NOT NEEDED
        #     index_pop += 1 # Adding since the "indexing" for LinkedList technically starts at 1 if there's any value

        output = None

        current = self.head
        prev = None

        index = 0
        while index < index_pop: # Loop until the index meets index_pop;
            print(f"Current index:{index}")
            prev = current
            current = current.next
            index += 1
        output = current

        next_node:Node = None
        if current is not None:
            if current.next != None:
                next_node:Node = current.next
        prev.set_next(next_node)

        self._count -= 1
        
        return output

    def size(self) -> int:
        return self._count
    
    def is_empty(self) -> bool:
        return self._count == 0
    
    def all_nodes(self):
        current = self.head

        list_nodes:list = []

        while current is not None:
            list_nodes.append(current.get_data())
            current = current.next
        return list_nodes