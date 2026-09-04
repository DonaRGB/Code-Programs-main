def first_non_repeating_char(s):
    if not s:
        return ""
    for i in s:
        if s.count(i) == 1:
            return i
    return ""

s = str(input("Enter string : "))
print("First non-repeating character :", first_non_repeating_char(s))