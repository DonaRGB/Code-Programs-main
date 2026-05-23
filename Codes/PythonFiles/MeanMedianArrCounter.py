def arrayMean(arr):
    arr_size = len(arr)
    s = 0
    for i in range(0,arr_size):
        s += arr[i]
    return float(s/arr_size)
def arrayMedian(arr):
    arr_size = len(arr)
    sorted(arr)
    #print(arr,"\n")
    if arr_size % 2 != 0:
        return float(arr[int(arr_size//2)])
    #print((arr_size-1)/2,arr_size/2,"\n")
    return float((arr[int((arr_size-1)/2)] + arr[int(arr_size/2)])/2.0)
arr = [1,3,2,6,7,3,2,0,9,3]
print(f"Mean = {arrayMean(arr)}, Median = {arrayMedian(arr)}")