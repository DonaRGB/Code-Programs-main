def last_occuring(arr,x):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == x:
            return i
    return -1
from random import randint as ri
arr = [ri(0,10) for _ in range(0,ri(3,10))]
x = ri(0,10)
print("Array :", arr)
print("Last occurrence of {} is at index : {}".format(x, last_occuring(arr, x)))