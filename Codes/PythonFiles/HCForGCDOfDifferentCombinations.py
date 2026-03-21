def hcf(a, b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf
def print_hcf_statement(a, b):
    print(f"The HCF of {a} and {b} is: {hcf(a, b)}")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print_hcf_statement(num1, num2)