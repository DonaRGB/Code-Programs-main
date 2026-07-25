def printarray(a):
    for n in a:
        print(n, end = " ")
def arrIntersection(a,b):
    m,n = len(a),len(b)
    i,j = 0,0
    intersection = []
    while i < m and j < n:
        if a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:
            j += 1
        else:
            intersection.append(b[j])
            i += 1
            j += 1
    if intersection == []:
        print("No intersection found")
    else:
        print("Intersection :", printarray(intersection))
from random import randint as ri
x = [ri(1,10) for _ in range(5)].sort()
y = [ri(1,10) for _ in range(5)].sort()
print("Original arrays :\n - a :",x,"\n - b :",y,"\n")
print("Intersection of a and b :",arrIntersection(x,y))