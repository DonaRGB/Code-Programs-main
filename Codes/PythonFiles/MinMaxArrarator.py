def minElement(arr):
    arr_size = len(arr)
    temp = a[0]
    for i in range(1,arr_size):
        temp = min(temp,arr[i])
    return temp
def maxElement(arr):
    arr_size = len(arr)
    temp = a[0]
    for i in range(1,arr_size):
        temp = max(temp,arr[i])
    return temp
a = [1,334,346,244,2445,87,45,467,98,65,1,0,4879]
print(f"Min = {minElement(a)}, Max = {maxElement(a)}")