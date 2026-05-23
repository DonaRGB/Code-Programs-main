def reverseArr(a):
    length = len(a)
    l = 0
    r = length - 1
    t = a[l]
    for i in range(int(length / 2) + 1):
        a[l] = a[r]
        a[r] = t
        l += 1
        r -= 1
        t = a[l]
    return a
arr = [12,324,532,53,22]
print("Original Array :",arr)
print("Reversed Array :",reverseArr(arr))