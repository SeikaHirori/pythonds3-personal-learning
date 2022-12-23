import turtle

def tree(branch_len:int,t:turtle.Turtle):
    print(f"=== new recursive call. Current branch_len: {branch_len} ===", file=f)
    if branch_len > 5:
        t.forward(branch_len)
        print(f"phase 1: {branch_len}", file=f)
        t.right(20)
        tree(branch_len - 15, t)
        print(f'Phase 2 after subtracting by -15: {branch_len}', file=f)
        t.left(40)
        tree(branch_len - 15, t)
        print(f'Phase 3 after subtracting by 15 again: {branch_len}', file=f)
        t.right(20)
        t.backward(branch_len)
        print(f"last call of branch_len: {branch_len}", file=f)
    
    print("\n \n")

if __name__ == '__main__':
    with open("output.txt", "w") as f:
        print('Starting program \n', file=f)

        t:turtle.Turtle = turtle.Turtle()
        my_win = turtle.Screen()
        t.left(90)
        t.up()
        t.backward(100)
        t.down()
        t.color("green")
        tree(75, t)
        my_win.exitonclick()

        print(f"Ending program", file=f)