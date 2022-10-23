""" Activity: 3.9.2.1 Converting Infix Expressions to Postfix Expressions (intopost)

Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/InfixPrefixandPostfixExpressions.html
"""

from infix_to_postfix import convert

def test_set_1():
    infix_expr:str = "A * B + C * D"
    output = convert.infix_to_postfix(infix_expr)
    assert output == "A B * C D * +"

def test_set_2():
    infix_expr:str = "( A + B ) * C - ( D - E ) * ( F + G )"
    output = convert.infix_to_postfix(infix_expr)
    assert output == "A B + C * D E - F G + * -"