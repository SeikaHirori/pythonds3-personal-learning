
def to_str(n, base) -> str:
    convert_string = "0123456789ABCDEF"
    
    if n < base:
        return convert_string[n]
    
    return to_str(n // base, base) + convert_string[n % base]