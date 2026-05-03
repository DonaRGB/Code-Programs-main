def maxNumOfArr(arr):
    if len(arr) in [0,1]:
        return arr[0]
    return max(arr[0],maxNumOfArr(arr[1:]))
def pmnoa(arr):
    print(f"The largest number of {arr} is {maxNumOfArr(arr)}.")
from random import randint as ri
l = ri(1,1000)
a = []
for _ in range(l):
    a.append(ri(1,1000*l))
pmnoa(a)