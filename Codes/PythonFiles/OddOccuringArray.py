def OddOccuringNum(arr):
    res = 0
    for e in arr:
        res ^= e
    return res
arr = []
n = int(input("Input the length of the array : "))
while n:
    num = int(input("Enter an element : "))
    arr.append(num)
    n -= 1
print("\nOdd Occuring Number is",OddOccuringNum(arr))