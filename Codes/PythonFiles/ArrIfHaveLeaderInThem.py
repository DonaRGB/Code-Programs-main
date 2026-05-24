def ifLeader(a):
    size = len(a)
    cmax = a[size-1]
    print(cmax)
    for i in range(size-2,-1,-1):
        if cmax < a[i]:
            print(a[i])
            cmax = a[i]
a = [1,443,53,43,5,24,1000]
ifLeader(a)