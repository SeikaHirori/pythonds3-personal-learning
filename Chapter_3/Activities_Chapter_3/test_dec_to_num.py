from unicodedata import decimal
from dec_to_num import convert, activity_3_8_2

def test_converting():
    conversion:convert = convert()
    decimal_num:int = 42
    assert conversion.divide_by_2(decimal_num) == "101010"

    decimal_num = 31
    assert conversion.divide_by_2(decimal_num) == "11111"

def test_activity_3_8_2():
   class_activity_3_8_2:activity_3_8_2 = activity_3_8_2()
