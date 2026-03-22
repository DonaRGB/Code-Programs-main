def check_if_prime(num):
    if num > 1:
        for i in range(2,int(num/2)+1):
            if num % i == 0:
                print(num,"is not a prime number.")
        print(num,"is a prime number.")
    else:
        print(num,"is not a prime number.")
n = int(input("Enter a number to check whether it is prime or not : "))
print("\n")
check_if_prime(n)