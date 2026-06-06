def k(a):
    n = len(a)
    msf = 0
    meh = 0
    for i in range(0,n):
        meh += a[i]
        if meh < 0:
            meh = 0
        if msf < meh:
            msf = meh
def mcsa(a):
    n = len(a)
    mk = k(a)
    mw = 0
    for i in range(0,n):
        mw += a[i]
        a[i] = -a[i]
    mw += k(a)
    if mw > mk:
        return mw
    return mk
from random import randint as ri
a = [ri(-5000,1000) for _ in range(0,ri(10,100))]
print(f"Array : {a}\nLargest Sum of Circular Array : {mcsa(a)}")