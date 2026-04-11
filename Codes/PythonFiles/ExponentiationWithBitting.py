def expUsingBase2(x,y):
    result = 1
    while y > 0:
        if y % 2 == 0:
            x **=2
            y >>= 1
            continue
        result *= x
        y = y - 1
    return result
x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
print(x,"^",y,"=",expUsingBase2(x,y))