""" 3.23. Implementing an Ordered List¶
    - Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementinganOrderedList.html
"""
import pytest
from orderedlist_example import OrderList as odl

def finish_your_test():
    assert 'finish your test' == 'ガンベリ！'





def test_add():
    o:odl = odl()
    finish_your_test()

def test_remove():
    o:odl = odl()
    finish_your_test()

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
    assert o.is_empty() == True

    o.add(300)
    assert o.is_empty() == False

def test_size():
    o:odl = odl()
    assert o.size() == 0

    o.add(2)
    assert o.size() == 1

def test_index():
    o:odl = odl()
    finish_your_test()

def test_pop():
    o:odl = odl()
    finish_your_test()
