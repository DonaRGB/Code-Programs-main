def findLength(arr):
    if len(arr) in [0,1]:
        return 1
    return 1 + findLength(arr[1:])
def pfl(arr):
    print(f"The length of the list {arr} is {findLength(arr)}.")
from random import randint as ri
l = ri(1,100)
a = [ri(1,100) for _ in range(l)]
pfl(a)