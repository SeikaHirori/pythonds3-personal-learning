""" 3.21.2. The UnorderedList Class
- Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementinganUnorderedListLinkedLists.html#the-unorderedlist-class
"""
import pytest
import _pytest.capture as pycap
from unorderedList_example import UnorderedList
from node_example import Node

def finish_your_test():
    assert "Finish writing your test!" == "You got this :3"

def debug_print_list_of_nodes(item):
    debug_previous_node:Node = Node(-1)
    debug_current_node:Node = item
    count:int = 1
    while debug_current_node is not None:
        print(f"\n===Counter: {count}===")
        print(f"Previous: {debug_previous_node.data}")
        print(f"Current head's item: {debug_current_node.data}")
        debug_previous_node = debug_current_node
        debug_current_node = debug_current_node.next

        if debug_current_node != None:
            print(f"New head: {debug_current_node.data}")
        count += 1
    print(f"\n :3 | Finished printing Nodes | :3")
    print("___ next step :3 ___")

def test_is_empty():
    u = UnorderedList()
    assert u.is_empty() == True


def test_add():
    u = UnorderedList()
    u.add(1)
    assert u.head.data == 1
    assert u.tail.data == 1

    u.add(31)
    assert u.head.data == 31
    next_item:Node = u.head.next
    assert next_item.data == 1
    assert u.tail.data == 1


def test_size():
    u = UnorderedList()
    u.add(2)
    u.add(2)
    u.add(1)
    u.add(10)

    assert u.size() == 4

def test_search():
    u = UnorderedList()
    request_item:int = 20

    output:bool = u.search(item=request_item)
    assert output == False

    u.add(41)
    u.add(20)
    u.add(30)
    output = u.search(item=request_item)
    assert output == True

def test_remove():
    u:UnorderedList = UnorderedList()
    added_item:int = 141
    requested_item:int = 141
    remove_item:int = 141

    # When the list is initalized, it's empty. The target item isn't there when searched.
    assert u.search(item=requested_item) == False

    # When the list adds items, the targeted item existed when searched.
    u.add(item=12)
    u.add(item=added_item)
    u.add(item=123)
    assert u.search(item=requested_item) == True

    # Remove the targeted item from the UL
    u.remove(remove_item)
    assert u.search(item=requested_item) == False

def test_remove_raise_Value_error(): # 
    u:UnorderedList = UnorderedList()
    remove_item:int = 121
    
    # When the Unordered List (UL) is empty
    with pytest.raises(Exception) as e_info:
        u.remove(remove_item)
    
    # When UL has some entries, but the targeted item is still not in the list.
    u.add(131)
    u.add(2910)
    with pytest.raises(Exception) as e_info:
        u.remove(remove_item)

def test_append_O_n(): # TODO
    """# Self-check #1"""
    u:UnorderedList = UnorderedList()    
    u.append_O_n(item=21)
    assert u.search(item=21) == True
    debug_print_list_of_nodes(u.head)

    u.append_O_n(item=310)
    debug_print_list_of_nodes(u.head)

    u.append_O_n(item=910)
    requested_item_1:int = 910
    output = u.search(item=requested_item_1)
    assert output == True


    requested_item_2:int = 21
    output = u.search(item=requested_item_2)
    assert output == True

    debug_print_list_of_nodes(u.head)


def test_append_O_1():
    """# Self-check #2
    
    - Add instance variable that is the last variable
    """
    u:UnorderedList = UnorderedList()
    u.append_O_1(1)
    assert u.head.data == 1
    assert u.tail.data == 1
    assert u._count == 1
    
    u.append_O_1(2)
    assert u.tail.data == 2
    assert u._count == 2

    u.append_O_1(3)
    u.append_O_1(4)

    result = u.search(3)
    assert result == True



def test_insert(capsys:pycap.CaptureFixture): # TODO
    # RFER 4 | assigning type for capsys
    u:UnorderedList = UnorderedList()
    u.insert(item=300, pos=0)
    result:bool = u.search(300)
    assert result == True

    u.insert(item=999, pos=999)
    captured = capsys.readouterr()
    assert captured.out == "pos (1000) is out of bounds\n", "After adding 1 to pos in the function, pos should be 1000."

    u.add(1)
    u.add(20)
    result = u.all_nodes()
    assert result == [20, 1, 300]

    u.insert(item=4000, pos=1)
    result = u.size()
    assert result == 4
    result = u.index(4000)
    output_all_nodes = u.all_nodes()
    assert result == 1, f"The int value (4000) was not found in the list. The list has: {output_all_nodes}"
    assert output_all_nodes == [20, 4000, 1, 300], f"The list has: {output_all_nodes}"

    u.insert(item=50000, pos=-2)
    result = u.search(item=50000)
    assert result == False

def test_new_tail():
    u:UnorderedList = UnorderedList()

    # Test insert() when list is empty
    u.insert(pos=0, item=0)
    assert u.tail.data == 0

    u.add(20)
    # Test insert()
    u.insert(pos=2, item = 300)
    assert u.tail.data == 300

    # Test append()
    u.append_O_1(item=4000)
    assert u.tail.data == 4000

    # Test pop()
    


def test_index():
    u:UnorderedList = UnorderedList()

    u.add(1)
    u.add(1)
    u.add(2)
    u.add(3)

    assert u.index(1) == 2
    assert u.index(2) == 1
    assert u.index(3) == 0


def test_pop():
    u:UnorderedList = UnorderedList()

    u.add(1)
    u.add(4)
    u.add(9)
    u.add(12)
    u.add(20)

    assert u.head.get_data() == 20

    output_pop:Node = u.pop()
    output_size:int = u.size()
    output_index:int = u.index(4)
    assert output_size == 4, f'Size was {output_size}. The size should be 4 after using pop()'
    assert output_index == 3, f'Index of element 1 was {output_index}. The index should be 3 after using pop().'
    assert u.all_nodes() == [20, 12, 9, 4]
    assert output_pop.get_data() == 1 # FIXME

    # Index should be less than 0
    output_pop = u.pop(index_pop=-2)
    assert u.all_nodes() == [20, 12, 4]
    assert output_pop.get_data() == 9

    # Index should be greater than or equal to 0
    output_pop = u.pop(2)
    assert u.all_nodes() == [20, 12]
    assert output_pop.get_data() == 4

    # Empty out the list
    u.pop()
    u.pop()
    assert u.all_nodes() == []
    assert u.is_empty() == True, f"There are still entries in the linked list. They are:\n {u.all_nodes()}"



def test_size():
    u:UnorderedList = UnorderedList()
    assert u.size() == 0

    u.add(1)
    assert u.size() == 1

    u.append_O_1(2)
    u.append_O_1(3)
    u.append_O_1(4)
    u.append_O_1(5)
    assert u.size() == 5

def test_is_empty():
    u:UnorderedList = UnorderedList()
    
    assert u.is_empty() == True

    u.add(1)
    assert u.is_empty() == False

    u.remove(1)
    assert u.is_empty() == True
