def rotations(a,n):
    size = len(a)
    for _ in range(n):
        rotate(a)
def rotate(a):
    size = len(a)
    t = a[0]
    for i in range(size-1):
        a[i] = a[i+1]
    a[size-1] = t
def printArr(a):
    for i in range(len(a)):
        print("% d"% a[i], end = " ")
    print("\n")
a = [1,12,2,3,4,756,54,34,3]
printArr(a)
rotations(a,2)
printArr(a)