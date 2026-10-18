def is_substring(s,ss):
    if ss in s:
        return s.index(ss)
    return -1
st = str(input("Enter a string : "))
sub = str(input("Enter a substring : "))
iss = is_substring(st,sub)
if iss != -1:
    print(f"Substring \"{sub}\" found at index \"{iss}\" in string \"{st}\".")
else:
    print("Substring not found in string!")