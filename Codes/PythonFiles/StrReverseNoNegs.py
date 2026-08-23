def reverse_str(s:str):
    ns = ""
    s = str(s)
    for i in range(len(s)):
        ns = s[i] + ns
    return ns
string = "Hello, World!"
print("Original String :",string)
print("Reversed String :",reverse_str(string))