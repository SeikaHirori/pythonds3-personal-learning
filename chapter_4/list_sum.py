

def loop_list_sum(num_list:list[int]):
    output_sum:int = 0
    while num_list:
        output_sum += num_list.pop()
    return output_sum

def recurison_list_sum(num_list:list[int]):
    if len(num_list) == 1:
        return num_list[0]
    
    return num_list[0] + recurison_list_sum(num_list=num_list[1:])