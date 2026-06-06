def lsoaoeao(arr):
    if not arr:
        return 0
    cs = 0
    bs = 0
    bl = 0
    cl = 0
    for i in range(1,len(arr)):
        if arr[i] & 1 != arr[i-1] & 1:
            cl += 1
        else:
            cl = 1
            cs = i
        if cl > bl:
            bl = cl
            bs = cs
    return arr[bs:bs+bl]
from random import randint as ri
a = [ri(0,10000) for _ in range(0,ri(10,100))]
l = lsoaoeao(a)
print(f"Array : {a}\nLongest Sequence of Alternation of Evenity and Odd : {l}\nLength : {len(l)}")