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


