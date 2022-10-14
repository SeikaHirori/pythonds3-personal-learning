""" Activity: 3.8.1 Converting from Decimal to Binary (divby2)
    Section: 3.8. Converting Decimal Numbers to Binary Numbers¶ 

Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html#lst-binconverter

"""

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
        
        bin_string:str = ""
        while not rem_stack.is_empty():
            bin_string = bin_string + (str(rem_stack.pop()))
        
        return bin_string

class activity_3_8_2:
    def base_converter(self, decimal_num, base):
        digits:str = "0123456789ABCDEF"
        rem_stack:Stack = Stack()

        while decimal_num > 0:
            print(f"Decimal value: {decimal_num}")

            rem = decimal_num % base
            print(f"Rem value:{rem}")

            rem_stack.push(rem)
            decimal_num = decimal_num // base
            print(f"Decimal_num value: {decimal_num}")
            print("======")
        
        new_string:str = ""
        while not rem_stack.is_empty():
            new_string = new_string + digits[rem_stack.pop()]
            print(new_string)
            print("======")
        
        return new_string