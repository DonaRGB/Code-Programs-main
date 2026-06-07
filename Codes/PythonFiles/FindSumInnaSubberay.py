def find_sum_in_subarray(a,s):
    n = len(a)
    for i in range(0,n):
        cs = a[i]
        j = i + 1
        while j <= n:
            if cs == s:
                print(f"Sum found between indexes {i} and {j-1}")
                return 1
            if cs > s or j == n:
                break
            cs += a[j]
            j += 1
    print("No subarray found.")
    return 0
from random import randint as ri
a = [ri(-10,10) for _ in range(0,ri(5,10))]
s = ri(-5,20)
print(f"Array : {a}")
print(f"Sum to find : {s}")
find_sum_in_subarray(a,s)