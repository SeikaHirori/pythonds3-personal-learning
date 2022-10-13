from balanced_parentheses import par_checker

def test_set_1():
    symbol_string:str = "((()))"

    assert par_checker().par_checker(symbol_string) == True

def test_set_2():
    symbol_string:str = "((()()))"

    assert par_checker().par_checker(symbol_string) == True

def test_set_3():
    symbol_string:str = "(()"

    assert par_checker().par_checker(symbol_string) == False

def test_set_4():
    symbol_string:str = ")("

    assert par_checker().par_checker(symbol_string) == False