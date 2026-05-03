def checkIfSorted(arr):
    l = len(arr)
    if l in [0,1]:
        return True
    return a[0] <= a[1] and checkIfSorted(a[1:])
def pcis(arr):
    if checkIfSorted(arr):
        print(f"\nYes, {arr} is a sorted list.")
        return
    print(f"\nNo, {arr} is not a sorted list")
from random import randint as ri
l = ri(1,10)
a = []
for i in range(l):
    a.append(ri(i,l))
    if a[-1] == l:
        break
    i = a[-1]
pcis(a)