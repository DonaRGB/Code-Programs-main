def if_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]
def print_palindrome_statement(num):
    if if_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
number = int(input("Enter a number: "))
print_palindrome_statement(number)