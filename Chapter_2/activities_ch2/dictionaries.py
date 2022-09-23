"""
    Link: https://runestone.academy/ns/books/published/pythonds3/AlgorithmAnalysis/Dictionaries.html
"""

from timeit import Timer
import random

# Listings 6
print(f"{'n':10s}{'list':>10s}{'dict':>10s}")
for i in range(10_000, 1_000_001, 20_000):
    t = Timer(f"random.randrange({i}) in x", "from __main__ import random, x")
    
    x = list(range(i))
    list_time = t.timeit(number=1000)

    x = {j: None for j in range(i)}
    dict_time = t.timeit(number=1000)

    print(f"{i:<10} {list_time:>10.3f} {dict_time:>10.3f} ")