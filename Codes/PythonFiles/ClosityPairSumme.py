MAX_VALUE = 1000000
def findClosestPairSum(arr, s):
    n = len(arr)
    res_l, res_r = 0, 0
    l,r,d = 0, n-1, MAX_VALUE
    while l < r:
        if abs(arr[l] + arr[r] - s) < d:
            res_l, res_r = l, r
            d = abs(arr[l] + arr[r] - s)
        if arr[l] + arr[r] > s:
            r -= 1
        else:
            l += 1
    print(f"Closest Pair: [{arr[res_l]}, {arr[res_r]}] with sum {arr[res_l] + arr[res_r]}")
from random import randint as ri
arr = [ri(1,100) for i in range(ri(10,25))]
arr.sort()
v = ri(25,100)
print(f"Array: {arr}\nValue: {v}")
findClosestPairSum(arr, v)