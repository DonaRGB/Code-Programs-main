def rotations(a,n):
    for _ in range(n):
        rotate(a)
def rotate(a):
    size = len(a)
    t = a[0]
    for i in range(size - 1):
        a[i] = a[i + 1]
    a[size - 1] = t
def ordinal_number(d:int):
    de = str(d)[-1]
    if len(str(d)) > 1 and str(d)[-2] == "1":
        return f"{d}th"
    if de == "1":
        return f"{d}st"
    elif de == "2":
        return f"{d}nd"
    elif de == "3":
        return f"{d}rd"
    else:
        return f"{d}th"
l = int(input("Enter the length of the array : "))
a = []
for i in range(l):
    a.append(int(input(f"Enter the {ordinal_number(i + 1)} element : ")))
print("\nOriginal Array :",a)
n = int(input("Enter the number of rotations : "))
rotations(a,n)
print(f"Rotated Array {n} time(s) :",a)