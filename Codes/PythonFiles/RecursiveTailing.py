def printRT(s,e):
    if s > e:
        return
    print(s)
    printRT(s+1,e)
n = int(input("Enter a value for n for printing from 1 to n : "))
printRT(1,n)