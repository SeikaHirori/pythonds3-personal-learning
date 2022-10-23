""" Activity: 3.9.2.1 Converting Infix Expressions to Postfix Expressions (intopost)

Link: https://runestone.academy/ns/books/published/pythonds3/BasicDS/InfixPrefixandPostfixExpressions.html
"""
from pythonds3.basic import Stack
class convert:
    def infix_to_postfix(infix_expr:str):
        prec:dict = {}
        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1

        op_stack:Stack = Stack()
        postfix_list:list = []
        token_list:list = infix_expr.split()

        print(token_list)

        for token in token_list:
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                postfix_list.append(token)
            elif token == "(":
                op_stack.push(token)
            elif token == ")":
                top_token = op_stack.pop()
                while top_token != "(":
                    postfix_list.append(top_token)
                    top_token  = op_stack.pop()
            else:
                while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                    postfix_list.append(op_stack.pop())
                op_stack.push(token)
        while not op_stack.is_empty():
            postfix_list.append(op_stack.pop())
        
        return " ".join(postfix_list) # Space is needed to achieve string "A B + C * D E - F G + * -". If space isn't there, result would be "AB+C*DE-FG+*-".

print(convert.infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))