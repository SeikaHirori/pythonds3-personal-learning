from pythonds3.basic import Stack

def to_str(n, base):
    the_stack:Stack = Stack()
    convert_string = "0123456789ABCDEF"

    while n > 0:
        if n < base:
            the_stack.push(convert_string[n])
        else:
            the_stack.push(convert_string[n % base])
        n = n // base

    output = ''
    while not the_stack.is_empty():
        output = output + str(the_stack.pop())

    return output