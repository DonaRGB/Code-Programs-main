def findMissingNum(a):
    n = len(a)
    total = (n + 1) * (n + 2) // 2
    sum_of_a = sum(a)
    return total - sum_of_a
n = int(input("Enter the size of the array : "))
cl = [i for i in range(1, n + 1)]
from random import randint as ri
from random import shuffle as sh
i = ri(0, n - 1)
cl.pop(i)
cl = sh(cl)
print("Original array :", cl)
print("Missing number :", findMissingNum(cl))