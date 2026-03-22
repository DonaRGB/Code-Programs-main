def is_prime(num : int):
    if not isinstance(num,int):
        raise TypeError(f"Expected int, got {type(num).__name__} instead.")
    if num > 1:
        for i in range(2,int(num/2)+1):
            if num % i == 0:
                return False
        return True
    return False
def double_digit_primes():
    for num in range(10,100):
        if is_prime(num):
            print(num)
print("All the double digit primes are :")
double_digit_primes()