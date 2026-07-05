def largestProduct(arr):
    if len(arr) < 2 or arr is None:
        return None
    a = 0
    b = 0
    for n in arr:
        if n > a:
            b = a
            a = n
        elif n > b:
            b = n
    return a,b
def imputArr():
    arr = []
    n = int(input("Enter the number of elements in the array : "))
    for i in range(n):
        arr.append(int(input(f"Enter element {i+1} : ")))
    return arr
arr = imputArr()
print("Original Array :",arr)
z = largestProduct(arr)
a = z[0]
b = z[1]
print(f"Numbers that make the largest product are : {a} * {b}")
print("Largest Product :",a*b)