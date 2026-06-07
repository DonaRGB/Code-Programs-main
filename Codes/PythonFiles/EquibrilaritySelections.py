def eqPnt(a):
    s = len(a)
    lss = 0
    rss = 0
    for i in range(s):
        lss = 0
        rss = 0
        for j in range(i):
            lss += a[j]
        for k in range(i + 1, s):
            rss += a[k]
        if lss == rss:
            return i
    return -1
from random import randint as ri
def generate_arr_no_repeat(l,range_v):
    a = []
    rs = []
    t = 0
    for _ in range(0,l):
        t = ri(range_v[0],range_v[1])
        while t in rs:
            t = ri(range_v[0],range_v[1])
        a.append(t)
        rs.append(t)
    return a
a = generate_arr_no_repeat(ri(10,100),[-100,100])
print(f"Array : {a}")
e = eqPnt(a)
print(f"Equilibrium Point Index : {e} (Value : {a[e] if e != -1 else 'N/A'})")