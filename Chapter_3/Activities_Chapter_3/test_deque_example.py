from deque_example import Deque

def test_1():
    d = Deque()

    assert d.is_empty() == True

    d.add_rear(4)
    d.add_rear('dog')
    d.add_front('cat')
    d.add_front(True)
    assert d.size() == 4
    assert d.is_empty() == False

    d.add_rear(8.4)
    assert d.remove_rear() == 8.4
    assert d.remove_front() == True
    assert d.peek_list() == ['dog', 4, 'cat']