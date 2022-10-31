from queue_example import Queue_example as que

def test_enqueue_and_dequeue():
    q = que()
    test_input_1:int = 4
    test_input_2:bool = True
    test_input_3:str = "How's your day?"

    q.enqueue(test_input_1)
    q.enqueue(test_input_2)
    q.enqueue(test_input_3)

    assert q.dequeue() == test_input_1
    assert q.dequeue() == test_input_2
    assert q.dequeue() == test_input_3

def test_is_empty_and_size():
    q = que()
    input_value:int = 3

    assert q.is_empty() == True
    assert q.size() == 0

    q.enqueue(input_value)

    assert q.is_empty() == False, "List should NOT be empty."
    assert q.size() == 1, "Size should be one."
