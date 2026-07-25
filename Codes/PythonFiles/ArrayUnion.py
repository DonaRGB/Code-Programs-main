def unionOfArr(a,b):
    m,n = len(a),len(b)
    i,j = 0,0
    while i < m and j < n:
        if a[i] < b[j]:
            print(a[i], end = " ")
            i += 1
        elif b[j] < a[i]:
            print(b[j], end = " ")
            j += 1
        else:
            print(b[j], end = " ")
            i += 1
            j += 1
    while i < m:
        print(a[i], end = " ")
        i += 1
    while j < n:
        print(b[j], end = " ")
        j += 1
from random import randint as ri
x = [ri(1,10) for _ in range(5)].sort()
y = [ri(1,10) for _ in range(ri(4,6))].sort()
print(f"Original arrays :\n - a : {x}\n - b : {y}\n")
print("Union of a and b :",unionOfArr(x,y))