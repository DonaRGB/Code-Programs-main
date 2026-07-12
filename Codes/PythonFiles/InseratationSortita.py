from random import randint as ri
a = [ri(1, 100) for _ in range(10)]
print("Original array :",a)
for i in range(1,len(a)):
    v = a[i]
    j = i - 1
    while j >= 0 and v < a[j]:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = v
print("Sorted array :",a)