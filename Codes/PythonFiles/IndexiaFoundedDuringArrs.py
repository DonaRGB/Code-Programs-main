def searchBinary(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    raise ValueError("Element not found in the array.")
from random import randint as ri
arr = [ri(0,100) for _ in range(ri(10,25))]
arr.sort()
target = ri(0,100)
try:
    res = searchBinary(arr, target)
    print("Array : {}".format(arr))
    print("Element {} is present at index {}.".format(target,res))
except ValueError as e:
    print("Error : {}".format(e))