def incanddec(s,e):
    if s < 1 or s > e:
        return
    print(s)
    incanddec(s-1,e)
    print(s)
n = int(input("Enter a value for n to generate a pattern from 1 to n and back down to 1 : "))
incanddec(n,n)