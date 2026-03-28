def isOddorEven(num):
    if num ^ 1 == n + 1:
        return True
    return False
num = int(input("Test a number to be even or odd : "))
print("\n")
if isOddorEven(num):
    print(num,"is even.")
else:
    print(num,"is odd.")