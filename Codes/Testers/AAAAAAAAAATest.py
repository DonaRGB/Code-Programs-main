from random import randint as ri
def very_random(s=0,e=100,t=500):
    z = 0
    for _ in range(t):
        z = ri(s,e)
    return z
def game_a(c):
    f = very_random(e=1000)
    if f <= 495:
        return c + 1
    return c - 1
def game_b(c):
    f = very_random(e=1000)
    if c % 3 == 0:
        if f <= 95:
            return c + 1
        return c - 1
    if f <= 745:
        return c + 1
    return c - 1
def main():
    c = 1000
    times = 0
    while c > 0:
        c = game_a(c)
        c = game_b(c)
        print(c,"\n")
        #times += 1
def list_segmentation(l,seg_point = -1):
    return l[:seg_point]
