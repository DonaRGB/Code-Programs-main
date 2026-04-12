def swap1(a,b):
    a ^= b
    b ^= a
    a ^= b
    print("After swapping : a =",a,", b =",b)
def swap2(a,b):
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a += (~b) + 1
    print("After swapping : a =",a,", b =",b)

a = 5
b = 10
print("Before swapping : a =",a,", b =",b)
swap1(a,b)
swap2(a,b)