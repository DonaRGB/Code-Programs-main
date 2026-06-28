def isPairSum(arr,s):
    n = len(arr)
    i = 0
    j = n-1
    while i < j:
        if arr[i] + arr[j] == s:
            return [arr[i], arr[j]]
        elif arr[i] + arr[j] < s:
            i += 1
        else:
            j -= 1
    return 0
from random import randint as ri
arr = [ri(1,100) for i in range(ri(10,25))]
arr.sort()
v = ri(25,100)
print(f"Array: {arr}\nValue: {v}\nPair: {isPairSum(arr, v)}")