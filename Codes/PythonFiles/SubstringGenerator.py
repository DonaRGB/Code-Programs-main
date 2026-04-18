def printSubstrings(s):
    s = str("".join(s.split()))
    r = []
    sn = set()
    n = len(str(s))
    for m in range(1, 1 << n):
        ss = ""
        for i in range(n):
            if m & (1 << i):
                ss += s[i]
        if ss not in sn:
            sn.add(ss)
            r.append(ss)
    return r
def printList(a):
    for i in a:
        print(f"    -> {i}")
s = str(input("Enter a string : "))
print("All substrings are : ")
printList(printSubstrings(s))