def li(l):
    arr = []
    print("\n")
    for i in range(l):
        arr.append(int(input(f"Enter the {i + 1}th element : ")))
    return arr
a = li(int(input("Enter the length of the array : ")))
print("Original Array :",a)
for i in range(len(a)):
    mi = i
    for j in range(i+1,len(a)):
        if a[mi] > a[j]:
            mi = j
    a[mi],a[i] = a[i],a[mi]
print("Sorted Array :",a)