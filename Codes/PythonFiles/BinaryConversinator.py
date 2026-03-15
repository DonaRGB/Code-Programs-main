
def str_to_int(strNum):
    number_string_list = ["0","1","2","3","4","5","6","7","8","9"]
    if type(strNum) == int:
        return strNum
    strNum = str(strNum)
    for c in strNum:
        if c not in number_string_list:
            raise Exception("Cannot have any characters other than numbers")
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
        else:
            t = 9
        intNum += t
    return intNum
def bin_to_dec(binNum:int):
    for i in str(binNum):
        if str_to_int(i) not in [0,1]:
            raise Exception("Base 2 does not have any other digit other than 0 or 1!")
    strt = str(binNum)
    result = 0
    l = len(strt)
    for idx in range(l - 1, -1, -1):
        #print(str_to_int(strt[idx]) * (2 ** (l - idx - 1)))
        result += str_to_int(strt[idx]) * (2 ** (l - idx - 1))
    return result
def dec_to_bin(decNum:int):
    if decNum == 0:
        return "0"
    result = ""
    while decNum > 0:
        result = str(decNum % 2) + result
        decNum //= 2
    return result