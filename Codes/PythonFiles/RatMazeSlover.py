def escapeWays(n,m,abc = {}):
    if n == 0 or m == 0:
        return 1
    if (n,m) in abc:
        return abc[(n,m)]
    abc[(n,m)] = (escapeWays(n-1,m,abc)+escapeWays(n,m-1,abc))
    return abc[(n,m)]
def paths(n,m,c=""):
    if n == 0 and m == 0:
        print(c)
        return
    if n > 0:
        paths(n-1,m,c+"D")
    if m > 0:
        paths(n,m-1,c+"R")
n = int(input("Enter the number of rows : "))
m = int(input("Enter the number of columns : "))
print(f"\nThere are {escapeWays(n,m)} ways to escape the {n} x {m} maze. The ways are :")
paths(n,m)