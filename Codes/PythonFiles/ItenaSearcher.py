def search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
from random import randint as ri
arr = [ri(0,10) for _ in range(0,ri(3,10))]
x = ri(0,10)
result = search(arr,x)
print(f"Array : {arr}")
print(f"Element to search : {x}")
if result != -1:
    print(f"Index of element : {result}")
else:
    print("Element not found.")