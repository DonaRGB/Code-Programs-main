import math as m
def printPowerSet(set_):
    powerSetSize = (int) (m.pow(2,len(set_)))
    for o in range(0,powerSetSize):
        for i in range(0,len(set_)):
            if (o & (1 << i)) > 0:
                print(set_[i],end = "")
        print("")
size = int(input("Enter array size : "))
set_ = []
for i in range(0,size):
    n = int(input("Enter an element : "))
    set_.append(n)
printPowerSet(set_)