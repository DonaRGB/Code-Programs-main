def calculateProfit(arr):
    size = len(arr)
    profit = 0
    for i in range(1,size):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
    return profit
from random import randint as ri
p = [ri(500,1000) for _ in range(0,ri(5,20))]
print("Max profit :",calculateProfit(p))