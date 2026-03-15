def print_factors(num:int):
    factors = [1]
    print("The factors of",num,"are :\n1")
    for i in range(2,(num // 2) + 1):
        if num % i == 0:
            factors.append(i)
            print(i)
    factors.append(num)
    print(num)
    return factors
number = int(input("Enter a number to look for its factors : "))
print_factors(number)