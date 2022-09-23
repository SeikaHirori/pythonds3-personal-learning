"""
    Link: https://runestone.academy/ns/books/published/pythonds3/AlgorithmAnalysis/Lists.html
"""

# Listing 3
from timeit import Timer

def test1():
    listo:list = []
    for i in range(1000):
        listo = listo + [i]

def test2():
    listo:list = []
    for i in range(1000):
        listo.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 = Timer("test1()", "from __main__ import test1")
print(f"concatenation: {t1.timeit(number=1000):15.2f} milliseconds ")

t2 = Timer("test2()", "from __main__ import test2")
print(f"appending: {t2.timeit(number=1000):19.2f} milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print(f"list comprehension: {t3.timeit(number=1000): 10.2f} milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print(f"list range: {t4.timeit(number=1000):18.2f} milliseconds")

print("======")
# Listing 4
pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
print(f"pop(0): {pop_zero.timeit(number=1000):10.5f} milliseconds")

x = list(range(2000000))
print(f"pop(): {pop_end.timeit(1000):11.5f} milliseconds")

