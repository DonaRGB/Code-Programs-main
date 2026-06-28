def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        s = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                s = True
        if not s:
            break
from random import randint as ri
arr = [ri(0,100) for _ in range(ri(25,50))]
print("Original Array :",arr)
narr = bubbleSort(arr)
print("New Sorted Array :",narr)