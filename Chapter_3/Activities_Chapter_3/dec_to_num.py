from pythonds3.basic import Stack

class convert:
    def divide_by_2(self, decimal_num) -> str:
        rem_stack = Stack()

        while decimal_num > 0:
            print(f"Decimal Value: {decimal_num}")
            
            rem = decimal_num % 2
            print(f"rem value: {rem}")
            
            rem_stack.push(rem)
            
            decimal_num = decimal_num // 2
            print(f"decimal value after '//': {decimal_num}")
            print("======")
        
        bin_strin:str = ""
        while not rem_stack.is_empty():
            bin_string = bin_string + (str(rem_stack.pop()))
        
        # return bin_string