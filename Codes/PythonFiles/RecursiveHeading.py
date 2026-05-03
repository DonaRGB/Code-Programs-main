def printRH(s,e):
    if s > e:
        return
    printRH(s+1,e)
    print(s)
n = int(input("Enter a value for n for printing 1 to n : "))
printRH(1,n)