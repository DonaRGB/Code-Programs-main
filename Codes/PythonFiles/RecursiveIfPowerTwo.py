def ifPower2(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return ifPower2(n/2)
    return False
n = int(input("Input a number :"))
if ifPower2(n):
    print(n,"is a power of 2.")
else:
    print(n,"is not a power of 2.")