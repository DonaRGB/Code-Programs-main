def numOfBits(n):
    o = 0
    z = 0
    while n:
        if n & 1 == 1:
            o += 1
        else:
            z += 1
        n >>= 1
    print("\n\nOnes :",o,"\nZeros :",z)
n = int(input("Enter your number : "))
numOfBits(n)