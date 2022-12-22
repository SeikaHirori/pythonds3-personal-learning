
def is_pal(s:str) -> bool:
    if len(s) == 0 or len(s) == 1:
        return True
    trimmed_original_s = remove_white(s)
    reverse_s = reverse_string(trimmed_original_s)

    return trimmed_original_s == reverse_s


def remove_white(s:str) -> str:
    return ''.join(char for char in s if char.isalpha()) # RFER 5

# def reverse_string(s:str) -> str: # Starting from back
#     if len(s) == 1:
#         return s[0]
    
#     return s[-1]+ reverse_string(s[:len(s) - 1])

def reverse_string(s:str) -> str:
    if len(s) == 1:
        return s[0]
    
    return reverse_string(s[1:]) + s[0]