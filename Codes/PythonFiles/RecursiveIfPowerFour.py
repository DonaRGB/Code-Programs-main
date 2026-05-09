def ifPower4(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 4 == 0:
        return ifPower4(n/4)
    return False
n = int(input("Input a number :"))
if ifPower4(n):
    print(n,"is a power of 4.")
else:
    print(n,"is not a power of 4.")