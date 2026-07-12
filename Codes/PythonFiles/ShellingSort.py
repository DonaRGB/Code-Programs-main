from random import randint as ri
a = [ri(1,100) for _ in range(ri(5,10))]
print("Original Array :",a)
n = len(a)
intvl = n // 2
while intvl > 0:
    for i in range(intvl,n):
        t = a[i]
        j = i
        while j >= intvl and a[j-intvl] > t:
            a[j] = a[j - intvl]
            j -= intvl
        a[j] = t
    intvl //= 2
print("Sorted Array :",a)