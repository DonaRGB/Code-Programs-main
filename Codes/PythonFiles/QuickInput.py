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
n = int(input("Enter the number of elements in the array : "))
a = []
for i in range(n):
    a.append(int(input("Enter the {} element : ".format(i+1))))
quickSort(a,0,n-1)
print("\nThe sorted array is : ",a)