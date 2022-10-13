from stacks import Stack

def test_Stack():
    """ Pseudocode: Test phases
    - Check if list is empty
    - Add 3 items to list check if: 
        - list is NOT empty
        - size of list is 3
        - peek at top value
    - Pop two items and check if:
        - correct items were grabbed from top of stack
        - list size is 1
        - peek at top value
    - Pop last item and check if:
            - last item is correct
            - list is FINALLY empty
    """
    
    stack_class = Stack()
    assert stack_class.is_empty() == True

    new_items:list[int] = ["hello", "world", ":3"]
    for item in new_items:
        stack_class.push(item)
    assert stack_class.is_empty() == False
    assert stack_class.size() == 3
    assert stack_class.peek() == ":3"

    item_3, item_2 = stack_class.pop(), stack_class.pop()
    assert item_3 == new_items[2]
    assert item_2 == new_items[1]
    assert stack_class.peek() == new_items[0]

    item_1 = stack_class.pop()
    assert item_1 == new_items[0]
    assert stack_class.is_empty() == True
