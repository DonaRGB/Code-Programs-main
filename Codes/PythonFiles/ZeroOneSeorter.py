def sortZerosAndOnes(arr):
    count0 = 0
    for num in arr:
        if num == 0:
            count0 += 1
    for i in range(count0):
        arr[i] = 0
    for j in range(count0,len(arr)):
        arr[j] = 1
from random import randint as ri
a = [ri(0,1) for _ in range(ri(10,50))]
print("Original Array :",a)
sortZerosAndOnes(a)
print("New Sorted Array :",a)