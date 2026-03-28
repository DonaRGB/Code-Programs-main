def numOfBits(n):
    count = 0
    while n:
        count += 1
        n >>= 1
    return count
num = int(input("Enter your number : "))
print("Total bits :",numOfBits(num))