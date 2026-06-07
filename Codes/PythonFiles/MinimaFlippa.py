def min_flips(a):
    n = len(a)
    zg = 0
    og = 0
    i = 0
    while i < n:
        v = a[i]
        if v == 0:
            zg += 1
        else:
            og += 1
        while i < n and a[i] == v:
            i += 1
    fv = 0 if zg < og else 1
    i = 0
    while i < n:
        if a[i] == fv:
            start = i
            while i + 1 < n and a[i+1] == fv:
                i += 1
            end = i
            print(f"Flip from {start} to {end}")
        i += 1
from random import randint as ri
a = [ri(0,1) for _ in range(0,ri(5,10))]
print(f"Array : {a}")
min_flips(a)