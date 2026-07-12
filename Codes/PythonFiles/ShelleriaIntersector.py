from random import randint as ri
a = [ri(1,100) for _ in range(ri(8,23))].sort()
b = [ri(1,100) for _ in range(ri(5,100))].sort()
m = len(a)
n = len(b)
i,j = 0,0
while i < m and j < n:
    if a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        print(b[j],end = " ")
        j += 1
        i += 1