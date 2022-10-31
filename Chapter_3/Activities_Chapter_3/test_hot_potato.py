from unicodedata import name
from hot_potato import potato as p

def test_1():
    name_list:list[str] = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    num:int = 7

    output = p().hot_potato(name_list=name_list, num=num)

    assert output == "Susan"