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
        return self._count == 0

    def add(self, item) -> None:
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

        if self.tail is None:
            self.tail = temp

        self._count += 1

    def size(self) -> int:
        # current = self.head
        # count:int = 0

        # while current is not None:
        #     # print(current)
        #     # print(f'Next: {current.next}')
        #     # print()
        #     count = count + 1
        #     current = current.next
        # return count
        return self._count

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


    def insert(self, item, pos:int=0) -> None: # Assume that the index/pos of an element starts at 0, which would be similar to Array/List # TODO
        if pos >= 0:
            pos += 1 # Add 1 to adjust the value to be in 
        else: # Insert doesn't take negative index
            return

        new_node:Node = Node(item)

        if self.is_empty(): # If list is empty
            self.head = new_node
            self.tail = new_node
        else:
            if pos > self.size(): # If pos is bigger than size()/ is out of bounds, exit immediately.
                print(f"pos ({pos}) is out of bounds")
                return 

            prev_node:Node = None
            current_node:Node = self.head

            index:int = 1
            while index < pos:
                prev_node = current_node
                current_node = current_node.next

                index += 1 
            print(f"Index: {index}")
                        
            new_node.set_next(current_node)
            prev_node.set_next(new_node)

        self._count += 1

    
    def index(self, item) -> int: 
        if self.head is None:
            return

        output:int = -1 
        
        current = self.head
        index = 0
        while current is not None:
            if current.get_data() == item:
                output = index
                break
            current = current.next
            index += 1

        if output <= -1:
            print(f"Index of targeted item was not found. Index was: {output}")
        return output

    def pop(self, index_pop:int=-1) -> Node:
        # The value from index_pop should be based on index starting at 0 for the first element
        # Default value for index_pop is last variable
        if self.is_empty():
            print(f"ERROR: The list is empty. Nothing was popped")
            return None

        if index_pop > self.size() - 1:
            # print(f"Value of index_pop ({index_pop}) exceeded the amount of items stored in linked list.")
            return None
        elif index_pop <= -1:
            while index_pop <= -1:
                index_pop += self.size()
        output:Node = None

        current:Node = self.head
        prev:Node = None
        index:int = 0
        while index < index_pop: # Loop until the index meets index_pop;
            prev = current
            current = current.next
            index += 1
        output = current

        next_node:Node = None
        if current.next != None:
            next_node = current.next
        if prev is not None:
            prev.set_next(next_node)
        if self.size() == 1:
            self.head = None

        # self.new_tail_check(current_node=current, new_node=next_node) # FIXME

        self._count -= 1
        
        return output
    
    def new_tail_check(self, index:int,new_node:Node) -> None: # TODO - Add check if the current node is the same object as the instance tail node. If so, set up a new tail from new node. 
        if index == self._count:
            self.tail = new_node
    
    def all_nodes(self):
        current = self.head

        list_nodes:list = []
        if current is None:
            return []

        while current is not None:
            list_nodes.append(current.get_data())
            current = current.next
        return list_nodes