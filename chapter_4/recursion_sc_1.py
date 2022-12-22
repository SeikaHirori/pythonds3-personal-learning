


def reverse(s):
    if len(s) == 0:
        return ''
    elif len(s) == 1:
        return s[0]
    return reverse(s[1::]) + s[0]