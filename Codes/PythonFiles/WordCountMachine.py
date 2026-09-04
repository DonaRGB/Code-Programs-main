def word_count(s):
    c = 0
    s.strip()
    for i in s:
        if i == " ":
            c += 1
    return c + 1

s = str(input("Enter string : "))
print("Word count :",word_count(s))