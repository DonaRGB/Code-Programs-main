from random import randint as ri
n = ri(25,50)
a = [ri(0,100) for _ in range(n)]
print("Original Array :",a)
for i in range(n):
    mi = i
    for j in range(i+1,n):
        if a[mi] > a[j]:
            mi = j
    a[mi],a[i] = a[i],a[mi]
print("Sorted Array :",a)