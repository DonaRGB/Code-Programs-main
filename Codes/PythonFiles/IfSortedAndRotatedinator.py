from random import randint as ri
l = ri(5,10)
a = [ri(1,l) for _ in range(l)]
c = 0
for i in range(l):
    if a[i-1] > a[i]:
        c += 1
if a[l-1] > a[0]:
    c += 1
print("Array :",a)
print("Is sorted and rotated? :",c <= 1)