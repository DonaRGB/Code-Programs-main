def secondLarge(arr):
    size = len(arr)
    l = sl = -2147483648
    for i in range(0,size):
        if arr[i] > l:
            sl = l
            l = arr[i]
        elif arr[i] > sl and a[i] != l:
            sl = a[i]
    print("Second Largest :",sl)
    return sl
a = [1,5,3,55,343,4,35,22,734,24,654,76,13,79,1324,86,324,213,789,24,75,985,596]
secondLarge(a)