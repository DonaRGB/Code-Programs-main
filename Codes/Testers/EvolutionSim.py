from AAAAAAAAAATest import very_random as vr
def evoMachine(nblrc,sus = 2500,generations = 255):
    if nblrc % 2 != 0:
        nblrc -= 1
    n = nblrc
    sn = nblrc // 2
    bn = nblrc // 2
    dr = 5 # measured in percent
    i = 0
    while sn > 0 and bn > 0 and i < generations:
        print(f"Generation {i+1} :")
        n = sn + bn
        if n > sus:
            dr = 75 - round((sus/n) * 1.05)
        else:
            dr = 5
        f = vr(e=1000)
        for _ in range(sn):
            if f <= dr * 0.85:
                sn -= 1
        for _ in range(bn):
            if f <= dr:
                bn -= 1
        sbn = 0
        bbn = 0
        for _ in range(sn):
            b = vr(0,5)
            sbn += b
        for _ in range(bn):
            b = vr(0,5)
            bbn += b
        sn = sbn
        bn = bbn
        i += 1
        print(" - Small Neeblers :",sn,"\n - Big Neeblers :",bn,"\n-------------------------------------")
    n = sn + bn
    if n == 0:
        print("All neeblers dead")
        return
    else:
        if sn == 0:
            print("All small neeblers dead")
            return
        print("All big neeblers dead")
def main():
    ip = 1000
    s = 10000
    print("Initial Population :",ip,"\n - Small Neeblers :",ip // 2,"\n - Big Neeblers :",ip // 2,"\n-------------------------------------")
    evoMachine(ip,s)

main()