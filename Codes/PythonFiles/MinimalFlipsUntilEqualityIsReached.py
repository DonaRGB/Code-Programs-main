def totalFlips(a,b):
    f = 0
    while a > 0 or b > 0:
        if (a & 1) != (b & 1):
            f += 1
        a >>= 1
        b >>= 1
    return f
def ptf(a,b):
    print(f"Total number of bit flips to make the numbers, {a} and {b}, equal is {totalFlips(a,b)}.")
def main():
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    ptf(num1,num2)
if __name__ == "__main__":
    main()