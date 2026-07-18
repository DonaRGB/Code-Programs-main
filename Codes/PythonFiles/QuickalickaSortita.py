def partition(a,l,h):
    p = a[h]
    i = l - 1
    for j in range(l,h):
        if a[j] <= p:
            i += 1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[h] = a[h],a[i+1]
    return i + 1
def quickSort(a,l,h):
    if l < h:
        pI = partition(a,l,h)
        quickSort(a,l,pI-1)
        quickSort(a,pI+1,h)
from random import randint as ri
a = [ri(5,100) for _ in range(ri(10,30))]
print("Unsorted array :",a,"\n")
n = len(a) - 1
quickSort(a,0,n)
print("Sorted Array :",a)