def bubbleSorting(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
def arrInputs():
    arr = []
    n = int(input("Enter the number of elements in the array : "))
    for i in range(n):
        arr.append(int(input(f"Enter element {i+1} : ")))
    return arr
a = arrInputs()
bubbleSorting(a)
print("\nSorted array is :",a)