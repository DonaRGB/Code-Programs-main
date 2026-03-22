def sieve_of_eratosthenes(num):
    start = 2
    primes = [True for _ in range(start,num + 1)]
    actual_primes = []
    p = 2
    while p * p <= num:
        if primes[p - start] == True:
            for i in range(p*p,num+1,p):
                primes[i] = False
        p += 1
    for p in range(2,num+1):
        if primes[p - start]:
            actual_primes.append(p)
            print(p)
    return actual_primes
num = int(input("Enter a number to test the Sieve of Eratosthenes on (it must be really big!) : "))
print("The following primes are smaller than or equal to",num)
sieve_of_eratosthenes(num)