def compare(n1,n2):
    return str(n1) + str(n2) > str(n2) + str(n1)
def largestNum(a):
    n = len(a)
    for i in range(n,0,-1):
        t = 0
        for j in range(i):
            if not compare(a[j],a[t]):
                t = j
        a[t],a[i-1] = a[i-1],a[t]
    return str(int("".join(map(str,a))))
from random import randint as ri
a = [ri(0,100) for _ in range(ri(25,50))]
print("Array :",a)
print("Largest Number :",largestNum(a))