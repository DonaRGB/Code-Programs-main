def arrInput():
    arr = []
    n = int(input("Enter the number of elements in the array : "))
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        arr.append(element)
    return arr
a = arrInput()
n = len(a)
intvl = n // 2
while intvl > 0:
    for i in range(intvl,n):
        t = a[i]
        j = i
        while j >= intvl and a[j-intvl] > t:
            a[j] = a[j - intvl]
            j -= intvl
        a[j] = t
    intvl //= 2
print("Sorted Array :",a)