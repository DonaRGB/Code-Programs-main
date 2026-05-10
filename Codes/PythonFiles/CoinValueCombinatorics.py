coins = list(reversed([1,5,10,100,500]))
def find_combinations(v,i=0,r = None):
    if r is None:
        r = [0] * len(coins)
    if i == len(coins) - 1:
        r[i] = v
        print("; ".join([f"{coins[j]} : {r[j]}" for j in range(len(coins))]))
        return
    coin = coins[i]
    for a in range(v//coin + 1):
        r[i] = a
        find_combinations(v - a*coin, i+1, r[:])
    
n = int(input("Enter the value of money to denominate : "))
print()
find_combinations(n)