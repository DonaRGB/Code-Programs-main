def setOrNot(num,n):
    if num & (1 << (n - 1)):
        print("\nSET")
    else:
        print("\nNOT SET")
num = int(input("Enter number : "))
n = int(input("Enter bit number : "))
setOrNot(num,n)