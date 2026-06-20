cities = ["New York City","Los Angeles","London","New York City","Phnom Penh","Mumbai","Toronto"]
target = "New York City"
def linear_search(sl,t):
    m = []
    for i in range(len(sl)):
        if sl[i] == t:
            m.append(i)
    if not m:
        raise ValueError("{} is not in the list.".format(t))
    else:
        return m
tsctys = linear_search(cities,target)
print("{} is present in the following locations in the list : {}".format(target,tsctys))