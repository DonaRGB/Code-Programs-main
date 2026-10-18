def sort_str(string):
    l = []
    a = ""
    for i in range(26):
        l.append(0)
    for i in range(len(string)):
        idx = ord(string[i])- ord("a")
        l[idx] += 1
    for i in range(26):
        if l[i] >= 1:
            for j in range(l[i]):
                a += chr(ord("a")+i)
    return a
s = str(input("Enter a string to sort : "))
print("Sorted String :",sort_str(s))