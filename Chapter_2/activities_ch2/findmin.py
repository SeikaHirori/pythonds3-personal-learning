

from re import I
import time
from random import randrange

def find_min(alist:list[int]): # This is n**2
    overallmin:int = alist[0]

    for i in alist:
        is_smallest = True
        for j in alist:
            if i > j:
                is_smallest = False
            if is_smallest:
                overallmin = i
    return overallmin

print(find_min([5,4,2,1,0]))
print(find_min([0,4,2,1,5]))

def find_min(alist): # This is linear
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar

for listSize in range(1000, 10001, 1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(find_min(alist))
    end = time.time()
    print(f"size: {listSize} time: {end - start}")