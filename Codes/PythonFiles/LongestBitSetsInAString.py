def str_to_int(strNum):
    # but really this can be put with any number
    number_string_list = ["0","1","2","3","4","5","6","7","8","9","-","."]
    if type(strNum) in [int, float]:
        return strNum
    strNum = str(strNum)
    if strNum[0] == "-":
        if strNum.count("-") > 1:
            raise Exception("Cannot have more than one negative sign.")
        sign = -1
        strNum = strNum[1:]
    else:
        sign = 1
    if strNum.count(".") > 1:
        raise Exception("Cannot have more than one decimal point.")
    for c in strNum:
        if c not in number_string_list:
            raise Exception("Cannot have any characters other than numbers")
    decimal_part = 0
    for i in range(-1*(len(strNum)-1),-1,-1):
        if strNum[i] == ".":
            decimal_part = len(strNum) - i - 1
            strNum = strNum[:i] + strNum[i+1:]
            break
    intNum = 0
    t = 0
    for i in strNum:
        intNum *= 10
        t = 0
        if i == "0":
            t = 0
        elif i == "1":
            t = 1
        elif i == "2":
            t = 2
        elif i == "3":
            t = 3
        elif i == "4":
            t = 4
        elif i == "5":
            t = 5
        elif i == "6":
            t = 6
        elif i == "7":
            t = 7
        elif i == "8":
            t = 8
        elif i == "9":
            t = 9
        intNum += t
    return (intNum * sign) / (10 ** decimal_part)
def dec_to_bin(decNum:int):
    if decNum == 0:
        return "0"
    result = ""
    while decNum > 0:
        result = str(decNum % 2) + result
        decNum //= 2
    return str_to_int(result)
def longest_set_bits(n):
    count = 0
    while n:
        n = n & (n << 1)
        count += 1
    return count

n = int(input("Enter a number to find the longest set bits in it : "))
print("The longest set bits in",n,"() is",longest_set_bits(n))