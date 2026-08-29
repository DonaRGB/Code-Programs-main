def remove_spaces(s):
    r = ""
    for i in range(len(s)-1):
        if s[i] == " ":
            continue
        elif s[i] == "\n" or s[i] == "\t":
            continue
        else:
            r += s[i]
    if s[-1] == " ":
        return r
    return r + s[-1]

i = str(input("Enter string : "))
print("No spaces :",remove_spaces(i))