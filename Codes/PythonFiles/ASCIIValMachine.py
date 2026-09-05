def findASCII(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = ord(i)
    return d

i = str(input("Enter a word : "))
print(findASCII(i))