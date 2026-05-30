def max_diff(a):
    if len(a) < 2:
        return -1
    s = l = a[0]
    for x in a[1:]:
        if x > l:
            l = x
        if x < s:
            s = x
    return l - s
from random import randint as ri
arr = [ri(0,100) for _ in range(0,ri(6,20))]
print("Array :",arr)
print("Maximum difference :",max_diff(arr))