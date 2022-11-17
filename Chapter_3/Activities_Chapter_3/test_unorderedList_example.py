""" 3.21.2. The UnorderedList Class
- Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementinganUnorderedListLinkedLists.html#the-unorderedlist-class
"""

from unorderedList_example import UnorderedList
from node_example import Node

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

    assert u.search(item=requested_item) == False

    u.add(item=12)
    u.add(item=added_item)
    u.add(item=123)
    assert u.search(item=requested_item) == True

    u.remove(remove_item)
    assert u.search(item=requested_item) == False

