def printTwoOdd(arr):
    size = len(arr)
    xorof2 = arr[0]
    x = 0
    y = 0
    setbit = 0
    for i in range(1,size):
        xorof2 ^= arr[i]
    setbit = xorof2 & ~(xorof2 - 1)
    for j in range(size):
        if arr[j] & setbit:
            x ^= arr[j]
            continue
        y ^= arr[j]
    print("The two odd occuring numbers are",x,"and",y)
arr = []
s = int(input("Enter the length of the array : "))
for _ in range(s):
    arr.append(int(input("Enter a number : ")))
printTwoOdd(arr)