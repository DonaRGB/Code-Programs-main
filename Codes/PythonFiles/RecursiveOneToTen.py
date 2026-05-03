def print1to10(start = 1,end):
    if start > end:
        return
    print(start)
    print1to10(start+1,end)

print1to10(end = 10)