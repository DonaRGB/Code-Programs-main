def arrIntersection(a,b):
    m,n = len(a),len(b)
    i,j = 0,0
    print("Intersection of a and b :")
    while i < m and j < n:
        if a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:
            j += 1
        else:
            print("- ",b[j])
            i += 1
            j += 1
from random import randint as ri
x = [ri(1,10) for _ in range(15)]
y = [ri(1,10) for _ in range(15)]
x.sort()
y.sort()
print("Original arrays :\n - a :",x,"\n - b :",y,"\n")
arrIntersection(x,y)