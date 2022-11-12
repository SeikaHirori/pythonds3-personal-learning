""" 3.21.1. The Node Class
    Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/ImplementinganUnorderedListLinkedLists.html#the-node-class
"""

class Node:

    def __init__(self, node_data) -> None:
        self._data = node_data
        self._next = None
