def roman_to_int(roman_string):
    roman = {
        "M":1000,
        "D":500,
        "C":100,
        "L":50,
        "X":10,
        "V":5,
        "I":1
    }
    resultInt = 0
    for i in range(0,len(roman_string) - 1):
        if roman[roman_string[i]] < roman[roman_string[i + 1]]:
            resultInt -= roman[roman_string[i]]
        else:
            resultInt += roman[roman_string[i]]
    return resultInt + roman[roman_string[-1]]
roman_num = str(input("Enter a roman numeral : "))
print(f"Integer equivalent : {roman_to_int(roman_num)}")






























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
def int_to_roman(intInput:int):
    maximum = 3999999
    if intInput < 1:
        raise Exception("Cannot have numbers less than 1!")
    if intInput > maximum:
        raise Exception("Cannot have numbers bigger than 3999!")
    strRoman = ""
    places = [i for i in range(maximum,0,-1)]
    roms = [["M̅"],["C̅","D̅"],["X̅","L̅"],["M","V̅"],["C","D"],["X","L"],["I","V"]]
    place = 0
    intInput = str(intInput)
    l = len(intInput)
    placet = 0
    subtract = l + 1
    placer = places[placet] - subtract
    for i in range(0,l):
        place = 0
        r = str_to_int(intInput[i])
        placet = -1 * l + 1
        placer += 1
        place = roms[placer]
        #print(r,"\n",placer,"\n",placet,"\n")
        if r < 4:
            strRoman += place[0] * r
        elif r == 4:
            strRoman += place[0] + place[1]
        elif r == 5:
            strRoman += place[1]
        elif 5 < r < 9:
            strRoman += place[1]
            strRoman += place[0] * (r - 5)
        elif r == 9:
            strRoman += place[0] + roms[placer - 1][0]
    return strRoman
#from random import randint as ri
#a = ri(1,3999)
#print(f"{a} -> {int_to_roman(a)}")f"{place[0]}{roms[placer - 1][0]}"