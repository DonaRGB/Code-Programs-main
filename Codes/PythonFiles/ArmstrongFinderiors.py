number = int(input("Enter a number to check if it is an Armstrong number : "))
digits  = len(str(number))
resultNum = 0
temp = number
while temp > 0:
    digit = temp % 10
    resultNum = digit ** digits
    temp //= 10
if resultNum == number:
    print(f"\n{number} is an Armstrong number.")
else:
    print(f"\n{number} is not an Armstrong number.")