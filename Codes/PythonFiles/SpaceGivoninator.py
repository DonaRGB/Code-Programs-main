from random import randint as ri
def sum_n(n):
    return (n * (n+1)) / 2
print("The sum of the first n numbers (n = 5) :",sum_n(5))

def array_space(a):
    total = 0
    for i in a:
        total += i
    return total
a = [ri(5,12),ri(12,488),ri(12,34),ri(1000,100348)]
print("Array sum :",array_space(a))

# this last one i do for fun :3
def sum_a_to_b(a = 1,b = 100):
    if a > b:
        return sum_n(a) - sum_n(b - 1)
    elif a < b:
        return sum_n(b) - sum_n(a - 1)
    else:
        return 0