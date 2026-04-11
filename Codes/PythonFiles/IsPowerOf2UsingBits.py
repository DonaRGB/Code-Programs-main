def isPowerOf2(n):
    if n <= 0:
        return False
    return (n & (~(n - 1))) == n
num = int(input("Enter a nunber : "))
if isPowerOf2(num):
    print(num,"is a power of 2.")
else:
    print(num,"is not a power of 2.")