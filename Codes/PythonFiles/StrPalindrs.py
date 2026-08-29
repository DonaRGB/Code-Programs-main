def is_palin(s):
    if s.lower() == s[::-1].lower():
        return True
    return False

s = str(input("Enter string : "))
print("Is Palindrome?",is_palin(s))