def func1(a = 1,b = 1):
    return a*b # in 1 iteration
def func2(a,b):
    sum = 0
    for i in range(a):
        for j in range(0,b):
            sum += 1
    return sum # in N iterations
def func3(a,b):
    sum = 0
    while a > 0:
        if a % 2 == 1:
            result += b
        a //= 2
        b *= 2
    return result # in log(N) iterations 
a = int(input("Enter the value for \"a\" : "))
b = int(input("Enter the value for \"b\" : "))
print("Function 1 :",func1(a,b))
print("Function 2 :",func2(a,b))