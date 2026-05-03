def recurseTillNeg():
    n = int(input("Enter a number : "))
    if n < 0:
        print("-ve")
        return
    else:
        print("+ve")
        recurseTillNeg()

recurseTillNeg()