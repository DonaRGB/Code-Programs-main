def remove_vowels(s):
    v = ["a","e","i","o","u"]
    r = ""
    for i in s:
        if i.lower() not in v:
            r += i
        else:
            r += " "
    return r

s = str(input("Input string : "))
print("Removed vowels :",remove_vowels(s))