from convert_int_to_string import *

def test_to_str():
    output = to_str(n=769, base=10)
    assert output == '769'
    
    output = to_str(n=1329, base=16)
    assert output == '531'

