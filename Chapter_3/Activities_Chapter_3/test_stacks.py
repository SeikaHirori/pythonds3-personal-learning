from stacks import Stack

def test_Stack():
    """ Pseudocode: Test phases
    - Check if list is empty
    - Add 3 items to list check if: 
        - list is NOT empty
        - size of list is 3
    - Pop two items and check if:
        - correct items were grabbed from top of stack
        - list size is 1
    - Pop last item and check if:
            - last item is correct
            - list is FINALLY empty
    """
    
    stack_class = Stack()
    assert stack_class.is_empty() == True

    new_items:list[int] = [1, 2, 3]
    for item in new_items:
        stack_class.push(item)
    assert stack_class.is_empty() == False
    assert stack_class.size() == 3
    assert stack_class.peek() == 

    item_3, item_2 = stack_class.pop(), stack_class.pop()

    assert item_3 == 3
    assert item_2 == 2
