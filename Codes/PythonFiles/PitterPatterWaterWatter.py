def findWaterHeight(wh):
    size = len(wh)
    lTlst = [0] * size
    rTlst = [0] * size
    w = 0
    lTlst = wh[0]
    for i in range(1,size):
        lTlst[i] = max(lTlst[i-1],wh[i])
    for i in range(size - 2,-1,-1):
        rTlst[i] = max(rTlst[i+1],wh[i])
    for i in range(0,size):
        w += min(lTlst[i],rTlst[i]) - wh[i]
    return w
from random import randint as ri
wtrs = [ri(0,3) for _ in range(0,ri(6,20))]
print("Water :",findWaterHeight(wtrs))