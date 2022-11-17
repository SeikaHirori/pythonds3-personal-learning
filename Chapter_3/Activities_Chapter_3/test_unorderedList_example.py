""" 3.21.2. The UnorderedList Class
- Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementinganUnorderedListLinkedLists.html#the-unorderedlist-class
"""
import pytest

from unorderedList_example import UnorderedList
from node_example import Node

def finish_your_test():
    assert "Finish writing your test!" == "You got this :3"

def test_is_empty():
    u = UnorderedList()
    assert u.is_empty() == True


def test_add():
    u = UnorderedList()
    u.add(1)
    assert u.head.data == 1

    u.add(31)
    assert u.head.data == 31
    next_item:Node = u.head.next
    assert next_item.data == 1


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

def test_append(): # TODO
    """# Self-check #1"""
    u:UnorderedList = UnorderedList()    
    u.append(item=21)
    assert u.search(item=21) == True

    requested_item:int = 910
    u.append(item=910)
    output = u.search(item=requested_item)
    assert output == True


def test_insert(): # TODO
    """# Self-check #2"""
    u:UnorderedList = UnorderedList()

    finish_your_test()

def test_index(): # TODO
    u:UnorderedList = UnorderedList()

    finish_your_test()

def test_pop(): # TODO
    u:UnorderedList = UnorderedList()

    finish_your_test()