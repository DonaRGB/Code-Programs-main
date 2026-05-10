def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    ts = 0
    os = 0
    if stairs >= 2:
        ts = ways(stairs - 2)
    os = ways(stairs - 1)
    return ts + os
s = int(input("Enter the number of steps : "))
print("Ways up by taking one or two steps at a time :",ways(s))