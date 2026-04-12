def divideBits(a,b):
    if b == 0:
        raise Exception("Cannot have any number divided by zero!")
    sign = -1 if (a < 0) ^ (b < 0) else 1
    a, b = abs(a), abs(b)
    q = 0
    t = 0
    for i in range(31,-1,-1):
        if (t + (b << i)) <= a:
            t += b << i
            q |= 1 << i
    return q

a = int(input("Enter a value of a for a/b : "))
b = int(input("Enter a value of b for a/b : "))
print("Result of",a,"/",b,"=",divideBits(a,b))