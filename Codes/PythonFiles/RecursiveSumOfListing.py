def sumList(arr):
    if len(arr) in [0,1]:
        return arr[0]
    return arr[0] + sumList(arr[1:])
def psl(arr):
    print("The sum of the list",arr,"is",sumList(arr))
from random import randint as ri
l = ri(1,100)
a = []
for _ in range(3,l+1):
    a.append(ri(1,ri(2,l)))
psl(a)