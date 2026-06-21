def binarySearchRecursive(arr,l,r,x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearchRecursive(arr,l,mid-1,x)
        else:
            return binarySearchRecursive(arr,mid+1,r,x)
    else:
        return -1
from random import randint as ri
arr = [ri(0,100) for _ in range(ri(10,25))]
arr.sort()
x = ri(0,100)
res = binarySearchRecursive(arr,0,len(arr-1),x)
print("Array : {}".format(arr))
if res != -1:
    print("Element {} is present at index {}.".format(x,res))
else:
    print("Element is not present in the array.")