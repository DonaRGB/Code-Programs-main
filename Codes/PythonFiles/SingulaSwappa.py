def sortArr(arr):
    if len(arr) <= 1:
        return
    x = -1
    y = -1
    p = arr[0]
    for i in range(1,len(arr)):
        if p > arr[i]:
            if x == -1:
                x = i - 1
                y = i
            else:
                y = i
        p = arr[i]
    swap(arr,x,y)
def swap(a,i,j):
    t = a[i]
    a[i] = a[j]
    a[j] = t
from random import randint as ri
def pickPointsSwap(arr):
    l = len(arr)
    arr.sort()
    i = ri(0,l-1)
    j = 0
    while j == i:
        j == ri(0,l-1)
    a = arr
    swap(a,i,j)
    return a
arr = [ri(1,10) for _ in range(ri(10,20))]
arr = pickPointsSwap(arr)
print("Original Array :",arr)
sortArr(arr)
print("Sorted Array :",arr)