def reverse_bits(num):
    r = 0
    for _ in range(len(str(num))):
        result = (result << 1) | n & 1
        n >>= 1
    return r
def str_to_int(strNum):
    num = 0
    for char in strNum:
        num = num * 10 + (ord(char) - ord("0"))
    return num
def dec_to_bin(num):
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return str_to_int(binary)
n = int(input("Enter a number : "))
print("The reverse of the bits of the number", n,f"({dec_to_bin(n)})","is :",reverse_bits(n),f"({dec_to_bin(reverse_bits(n))})")