""" 3.21.1. The Node Class
    Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementinganUnorderedListLinkedLists.html#the-node-class
"""

from node_example import Node

def test_data():
    n = Node(93)

    assert n.data == 93

    n.set_data(10)
    assert n.data == 10

def test_next():
    foo:Node = Node(93)
    assert foo.next == None

    bar:Node = Node(20)
    foo.set_next(bar.get_data())
    assert foo.next == 20