def isPowerOf4(n):
    if n == 0:
        return False
    count = 0
    if n & (~(n - 1)) == n:
        while n > 1:
            n >>= 1
            count += 1
        if count % 2 == 0:
            return True
        return False
    return False
num = int(input("Enter a nunber : "))
if isPowerOf4(num):
    print(num,"is a power of 4.")
else:
    print(num,"is not a power of 4.")