from balanced_symbols import balance_checker

def test_balance_checker():
    bal_check = balance_checker()
    symbol_string:str = '{({([][])}())}' # Set 1
    assert bal_check.balance_checker(symbol_string) == True

    symbol_string:str = '[{()]' # Set 2
    assert bal_check.balance_checker(symbol_string) == False