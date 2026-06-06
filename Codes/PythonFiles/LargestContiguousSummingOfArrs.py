def mSAS(a):
    size = len(a)
    m = -999999999999999999999999999999999999999999999999999999999999
    cmax = 0
    for i in range(0,size):
        cmax += a[i]
        if m < cmax:
            m = cmax
        if cmax < 0:
            cmax = 0
    return m
from random import randint as ri
a = [ri(-5000,1000) for _ in range(0,ri(10,100))]
print(f"Array : {a}\nLargest Sum of Array : {mSAS(a)}")