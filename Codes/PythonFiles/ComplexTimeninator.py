def prints(n):
    if n <= 0:
        return
    print("Sometextreally")
    prints(n // 2)
    prints(n // 2)
prints(128)