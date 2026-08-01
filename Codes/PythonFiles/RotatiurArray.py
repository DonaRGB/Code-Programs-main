def rotations(a,n):
    for _ in range(n):
        rotate(a)
def rotate(a):
    size = len(a)
    t = a[0]
    for i in range(size - 1):
        a[i] = a[i + 1]
    a[size - 1] = t
def printArr(a):
    for i in a:
        print("% d" % i, end = " ")
    print("\n")
from random import randint as ri
a = [ri(1,100) for _ in range(ri(5,10))]
print("Original Array :",printArr(a))
r = 2
rotations(a,r)
print(f"Rotated Array {r} time(s) :",printArr(a))