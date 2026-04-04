def checkIfEqual(num1,num2):
    if (num1 ^ num2) != 0:
        print("Numbers are not equal.")
        return
    print("Numbers are equal.")
num1 = int(input("Enter the first number to compare : "))
num2 = int(input("Enter the second number to compare : "))
checkIfEqual(num1,num2)