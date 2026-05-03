def factorial(n):
    if n in [0,1]:
        return 1
    return factorial(n-1) * n

i = int(input("Enter a number to find the factorial of : "))
print("The factorial of",i,"is :",factorial(i))