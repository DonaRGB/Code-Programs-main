def mergeSort(a):
    if len(a) > 1:
        m = len(a) // 2
        l = a[:m]
        r = a[m:]
        mergeSort(l)
        mergeSort(r)
        i = 0
        j = 0
        k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                a[k] = l[i]
                i += 1
            else:
                a[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            a[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            a[k] = r[j]
            j += 1
            k += 1
from random import randint as ri
a = [ri(1,100) for _ in range(ri(20,100))]
print("Unsorted Array :",a)
mergeSort(a)
print("Sorted Array :",a)