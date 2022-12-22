from list_sum import *

const_num_list:list[int] = [1, 3, 5, 7, 9]
const_result:int = 25

def test_loop_list_sum():
    output = loop_list_sum(num_list=const_num_list)
    
    assert output == const_result

def test_recursion_list_sum():
    output = recurison_list_sum(num_list=const_num_list)

    assert output == const_result