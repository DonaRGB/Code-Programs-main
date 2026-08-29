def case_flip(s):
    r = ""
    for i in s:
        if i.islower():
            r += i.upper()
        elif i.isupper():
            r += i.lower()
    return r

s = "ANnsndjNDjn J$ninNLnhb#J 42ouhJgUilF021D)YGSFyGFUYd!yFaGitD"
print(s)
print(case_flip(s))