def reverseStr(s):
    if len(s) == 1:
        return s[0]
    fc = s[0]
    return reverseStr(s[1:]) + fc
s = str(input("Enter something : "))
print("Reversed String :",reverseStr(s))