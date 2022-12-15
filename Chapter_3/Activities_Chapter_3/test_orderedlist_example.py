""" 3.23. Implementing an Ordered List¶
    - Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementinganOrderedList.html
"""
import pytest
from orderedlist_example import OrderList as odl
from node_example import Node

def finish_your_test():
    assert 'finish your test' == 'ガンベリ！'





def test_add():
    o:odl = odl()
    o.add(1)
    
    assert o._head.data == 1
    assert o._tail.data == 1
    assert o.size() == 1

    o.add(20)
    assert o._head.data == 1
    assert o._tail.data == 20
    assert o.size() == 2

    o.add(300)
    assert o._head.data == 1
    assert o._tail.data == 300
    assert o.size() == 3

def test_remove():
    o:odl = odl()

    o.add(1)
    o.add(20)
    o.add(300)
    o.add(4000)

    output = o.search(20)
    assert output == True, f"Result was {output}. Should be True after adding value 20."

    o.remove(20)
    output = o.search(20)
    assert output == False, f"Result was {output}. Should be False after removing value 20."


def test_search():
    o:odl = odl()
    assert o.search(9000) == False, "Empty list should return False"

    o.add(20)
    o.add(400)
    o.add(5000)
    o.add(1)
    assert o.search(20) == True, "Value '20' should be in list"

def test_is_empty():
    o:odl = odl()
    output = o.is_empty()
    assert output == True, f"Result was {output}. Should be True when the list is newly created."

    o.add(300)
    output = o.is_empty()
    assert output == False, f"Result was {output}. Should be False after adding value 300."

    o.remove(300)
    output = o.is_empty()
    assert output == True, f"Result was {output}. Should be True after removing value 300."

def test_size():
    o:odl = odl()
    output = o.size()
    assert output == 0, "Result was: {output}. New list should be 0"

    o.add(2)
    output = o.size()
    assert output == 1, f"Result was: {output}. List size should be 1 after one value"

    o.remove(2)
    output = o.size()
    assert output == 0, f"Result was {output}. List size should 0 after deleting value"

def test_index():
    o:odl = odl()
    
    o.add(1)
    o.add(20)
    o.add(300)

    assert o.index(1) == 0
    assert o.index(20) == 1
    assert o.index(300) == 2

    o.remove(20)
    assert o.index(20) == -1, "Value 20 should not be in the list."


def test_pop():
    o:odl = odl()

    o.add(1)
    o.add(20)
    o.add(300)
    o.add(4000)
    output = o.pop()
    assert output.data == 4000, f"Result was {output.data}. Should be 4000. Default pop should be the the last Node"

    output = o.pop(1)
    assert output.data == 20, f"Result was {output.data}. Should be 20 after popping with index 1."

    output = o.debug_all_node_values()
    assert output == [1,300]

def test_debug_all_node_values():
    o:odl = odl()
    output = o.debug_all_node_values()
    assert output == [], f"Result: {output}. Should be empty when list is empty."

    o.add(1)
    output = o.debug_all_node_values()
    assert output == [1]

    o.add(20)
    o.add(300)
    output = o.debug_all_node_values()
    assert output == [1, 20, 300]