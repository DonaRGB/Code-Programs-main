def isPairSum(arr, s):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if arr[i] + arr[j] == s:
                return [arr[i], arr[j]]
            if arr[i] + arr[j] > s:
                break
    return 0
from random import randint as ri
arr = [ri(1,100) for i in range(ri(10,25))]
arr.sort()
v = ri(25,100)
print(f"Array: {arr}\nValue: {v}\nPair: {isPairSum(arr, v)}")