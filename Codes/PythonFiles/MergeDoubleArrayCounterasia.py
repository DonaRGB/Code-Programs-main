def merge_sorted_arrs(a,b):
    i,j = 0,0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    while i < len(a):
        merged.append(a[i])
        i += 1
    while j < len(b):
        merged.append(b[j])
        j += 1
    return merged
from random import randint as ri
x = [ri(10,50) for _ in range(ri(10,50))]
y = [ri(10,50) for _ in range(ri(10,50))]
print(f"Original arrays :\n- {x}\n- {y}")
m = merge_sorted_arrs(x,y)
print("Sorted array :",m)