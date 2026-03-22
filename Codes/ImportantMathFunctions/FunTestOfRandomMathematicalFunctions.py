# for testing purposes only
from sys import exit as exit
from colorama import Fore as f
def summation(start,end):
    d = 1
    if end < start:
        d = -1
    c = 0
    for i in range(start,end+1,d):
        c += i
    return c
#Summation Theorum:
#If a < b:
#-difference between summation from a to b and summation from -a to b is exactly equal to a
#a = 12
#b = 430
#summation(a,b) - summation(-a,b) = a
def sm():
    z = [["q","w","e","r","t","y","u","i","o","p"],["a","s","d","f","g","h","j","k","l"],["z","x","c","v","b","n","m"]]
    for i in z:
        for j in i:
            if j != z[-1][-1]:
                if j != z[0][-1] and j != z[1][-1]:
                    print(j+",",end = "")
                else:
                    print(j+",")
            else:
                print(j)
#how to check for existing files for cv2.imwrite()
def generate_used_filenames(bp):
    from pathlib import Path
    b = Path(bp)
    i = 1
    nwp = b
    while nwp.exists():
        nwp = b.with_name(f"{b.stem}_{i}{b.suffix}")
        i += 1
    return str(nwp)
def date_ordinal_ender(d):
    de = str(d)[-1]
    if de == "1":
        return f"{d}st"
    elif de == "2":
        return f"{d}nd"
    elif de == "3":
        return f"{d}rd"
    else:
        return f"{d}th"
def time_ending_filename_generator(fn):
    from datetime import datetime as dt
    from pathlib import Path
    nwfn = Path(fn)
    date_time = dt.now().strftime(f"%A {date_ordinal_ender(dt.now().day)} %B %Y - %I:%M:%S %p")
    return str(f"{nwfn.stem}_{date_time}{nwfn.suffix}")
import os
ip = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","Pictures","test pic.jpg")
def factors_of_a_number(num : int):
    if not isinstance(num,int):
        raise TypeError(f"Expected int, got {type(num).__name__} instead.")
    fac = [1]
    for i in range(2,num,1):
        if num%i == 0:
            fac.append(i)
        else:
            pass
    fac.append(num)
    return fac
def pair_fac(num : int):
    if not isinstance(num,int):
        raise TypeError(f"Expected int, got {type(num).__name__} instead.")
    fac = factors_of_a_number(num)
    li = 0
    ri = -1
    pair_facs_list = []
    while len(fac) > 2:
        pair_facs_list.append([fac[li],fac[ri]])
        fac = fac[1:-1]
    if len(fac) == 2:
        pair_facs_list.append(fac)
    elif len(fac) == 1:
        pair_facs_list.append([fac[0],fac[0]])
    return pair_facs_list
def facrun():
    while True:
        try:
            num = int(input("Enter number : "))
            fac = factors_of_a_number(num)
            if len(fac) == 1:
                print(f"The factor of {num} is {fac[0]}.")
            elif len(fac) == 2:
                print(f"The factors of {num} are {fac[0]} and {fac[1]}.")
            elif len(fac) >= 3:
                print(f"The factors of {num} are",", ".join(map(str,fac[0:-1])),"and",str(fac[-1]) + ".")
        except ValueError as e:
            print(f"Error : {e}")
            break
def color_generator():
    from random import randint as r
    return (r(0,255),r(0,255),r(0,255))
def sieve_of_eratosthenes(num):
    start = 2
    primes = [True for _ in range(start,num + 1)]
    actual_primes = []
    p = 2
    while p * p <= num:
        if primes[p - start] == True:
            for i in range(p*p,num+1,p):
                primes[i] = False
        p += 1
    for p in range(2,num+1):
        if primes[p - start]:
            actual_primes.append(p)
            #print(p)
    return actual_primes
def is_prime(num : int):
    if not isinstance(num,int):
        raise TypeError(f"Expected int, got {type(num).__name__} instead.")
    if not num < 2:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    else:
        return False
def prime_fac(num : int):
    if not isinstance(num,int):
        raise TypeError(f"Expected int, got {type(num).__name__} instead.")
    prime = 1
    prime_factors = []
    store = num
    dp = nth_prime(prime)
    prime_loop = True
    while True:
        prime_loop = True
        if store == 1:
            break
        if store%dp == 0:
            prime_factors.append(dp)
            store /= dp
            continue
        else:
            prime += 1
            dp = nth_prime(prime)
            continue
    return prime_factors
def ask_for_prime_fac():
    try:
        num = int(input("Enter a whole number to prime factorise : "))
    except ValueError as ve:
        print("Error : {ve}")
        return
    str_of_sequence = [str(p) for p in prime_fac(num)]
    print(f"The prime factor(s) of {num} are {' × '.join(str_of_sequence)} | {num} = {' × '.join(str_of_sequence)}")
def country_order_randomizer():
    from random import shuffle as shuffle
    from random import randint as randint
    countries = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon","Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo","Costa Rica","Croatia","Cuba","Cyprus","Czech Republic","Democratic Republic of the Congo","Denmark","Djibouti","Dominica","Dominican Republic","East Timor","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Ivory Coast","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","North Korea","South Korea","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Macedonia","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]
    times = randint(10,200)
    randlist = countries
    for i in range(times+1):
        shuffle(randlist)
    the_str = ""
    for c in randlist:
        if c == randlist[len(randlist)-1]:
            the_str += str(c)
            break
        else:
            the_str += str(c)+","
    return randlist,the_str
def nth_prime(nth:int):
    if not isinstance(nth,int):
        raise TypeError(f"Expected int, got {type(nth).__name__} instead.")
    primes_list = []
    prime = 0
    while True:
        if is_prime(prime):
            primes_list.append(prime)
        if len(primes_list) == nth:
            return primes_list[-1]
        prime += 1
def show_nth_prime():
    try:
        num = int(input("Enter the term number of primes : "))
    except ValueError as e:
        raise TypeError(f"Expected int, got {type(num).__name__} instead.")
    prime = nth_prime(num)
    term = date_ordinal_ender(num)
    print(f"The {term} prime is {prime}.")
    return
from typing import Union as U
from decimal import Decimal
from fractions import Fraction
from numbers import Real
def add_all(*args:U[int,float,Decimal,Fraction]):
    the_sum = 0
    for i in args:
        if not (isinstance(i,Real) and type(i) is not bool):
            raise TypeError(f"Expected Real, got {type(i).__name__} instead.")
        the_sum += i
    return the_sum
def multiply_all(*args:U[int,float,Decimal,Fraction]):
    the_product = 1
    for i in args:
        if not (isinstance(i,Real) and type(i) is not bool):
            raise TypeError(f"Expected Real, got {type(i).__name__} instead.")
        the_product = i * the_product
    return the_product
def lcm(*args):
    nums = []
    for arg in args:
        if type(arg) not in [int] or type(arg) in [str,bool,complex,float]:
            raise Exception("The function only works with integers.")
            return
        if arg <= 0:
            raise Exception("The numbers cannot be zero or below.")
            return
        nums.append(arg)
    multiple = max(nums)
    is_divisible = True
    nums_divisible = []
    while is_divisible:
        for i in nums:
            if multiple % i != 0:
                multiple += 1
                continue
            else:
                nums_divisible.append(i)
        if len(nums_divisible) == len(nums):
            pass
        else:
            nums_divisible = []
            continue
        is_divisible = False
    return multiple
def gcf(*args):
    if not args:
        raise Exception("There are no numbers. Please add some.")
    result = args[0]
    if not isinstance(result,int) or isinstance(result,bool) or result <= 0:
        raise Exception("All numbers must be postive integers.")
    for n in args:
        if not isinstance(n,int) or isinstance(n,bool) or n <= 0:
            raise Exception("All numbers must be postive integers.")
        a,b = result,n
        while b != 0:
            a,b = b,a % b
        result = a
    return result
def farey_algorithm_mechanism(dec : float):
    from numbers import Real as Real
    from decimal import Decimal as Decimal
    from math import log10 as log
    from math import floor as mf
    from time import sleep as sleep
    lownum = 0
    lowden = 1
    highnum = 1
    highden = 1
    decpart = Decimal(str(dec))
    tempdec = Decimal(str(dec))
    sign = 1
    mednum = 0
    medden = 0
    dtk = -1 *(mf(log(decpart))) - 1
    decpart *= 10 ** dtk
    try:
        _ = tempdec < 0
        _ = tempdec + tempdec
    except TypeError:
        raise Exception("The number is not a number.")
    if tempdec < 0:
        sign = -1
        tempdec *= -1
    elif tempdec > 1:
        decpart = Decimal(str(tempdec - int(tempdec)))
    elif tempdec == 1:
        return 1,1,0,sign
    elif tempdec == 0:
        return 0,1,0,sign
    while True:
        mednum = lownum + highnum
        medden = lowden + highden
        if mednum == decpart * medden:
            return mednum,(medden * (10**dtk)),int(dec),sign
        else:
            if mednum < decpart * medden:
                lownum = mednum
                lowden = medden
            elif mednum > decpart * medden:
                highnum = mednum
                highden = medden
        #print(f"{mednum} / {medden} = {mednum/medden}\n{decpart}\n")
def farey_algorithm(dec : float):
    outs = farey_algorithm_mechanism(dec)
    num = outs[0]
    den = outs[1]
    whole = outs[2]
    sign = outs[3]
    gcfonad = gcf(num,den)
    num /= gcfonad
    den /= gcfonad
    num += (whole * den)
    num *= sign
    return int(num),int(den)
def farey_algorithm_show():
    from decimal import Decimal as Decimal
    try:
        dec = input("Enter a decimal number : ")
    except ValueError as e:
        raise Exception(f"Error : Input not number\n\n{e}\n------------------------------------------")
    num,den = farey_algorithm(Decimal(dec))
    print(f"{num} / {den} = {dec}")
def absolute_value(value):
    if value >= 0:
        return value
    else:
        return value * -1
def babylonian_square_root_method(root,estimation_assurance = 100):
    if root == 0:
        return 0
    n = 1
    while n*n < root:
        n += 1
    low_root = (n - 1) ** 2
    high_root = n * n
    estimate_root = 0
    if absolute_value(high_root - root) < absolute_value(root - low_root):
        estimate_root = n
    else:
        estimate_root = n - 1
    b = root - (estimate_root ** 2)
    x = b / (2 * estimate_root)
    root_calc = estimate_root + x
    for _ in range(0,estimation_assurance):
        estimate_root = root_calc
        b = root - (estimate_root ** 2)
        x = b / (2 * estimate_root)
        root_calc = estimate_root+x
        #print(f"Estimate Root : {estimate_root}\nRoot Calculated : {root_calc}\nX : {x}\n")
    return estimate_root
def babylonian_square_root_tolerance(root,tolerance = 1e-10):
    if root == 0:
        return 0
    x = root
    while True:
        next_x = (x+(root/x))/2
        if absolute_value(next_x - x) < tolerance:
            return next_x
        x = next_x
def error_calculation(value_gotten,true_value,is_percentage = True):
    error_value = absolute_value(value_gotten - true_value) / absolute_value(true_value)
    if is_percentage:
        return str(error_value * 100) + "%"
    else:
        return str(error_value)
def test_babylonian_method(num,error_is_percent_or_not = True):
    from math import sqrt as sqrt
    bsrm = babylonian_square_root_method(num)
    bsrt = babylonian_square_root_tolerance(num)
    rr = sqrt(num)
    print(f"{bsrm} | {rr} | Error : {error_calculation(bsrm,rr,error_is_percent_or_not)}")
    print(f"{bsrt} | {rr} | Error : {error_calculation(bsrt,rr,error_is_percent_or_not)}")
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
def comma_separation_in_numbers_function(num):
    num = str(num)
    if num[0] == "-":
        sign = "-"
        num = num[1:]
    else:
        sign = ""
    if "." in num:
        decpart = num.split(".")[1]
        num = num.split(".")[0]
    else:
        decpart = ""
    revnum = num[::-1]
    newnum = ""
    for i in range(len(revnum)):
        if i%3 == 0 and i != 0:
            newnum += ","
        newnum += revnum[i]
    return sign + newnum[::-1] + (("." + decpart) if decpart else "")
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
def hexadecimal_to_decimal(hex_str):
    hexDigits = "0123456789ABCDEF"
    hex_str = hex_str.upper()
    decimal = 0
    for i,digit in enumerate(reversed(hex_str)):
        value = hexDigits.index(digit)
        decimal += value * (16 ** i)
    return decimal
def decimal_to_hexadecimal(dec_num):
    if dec_num == 0:
        return "0"
    hexDigits = "0123456789ABCDEF"
    hex_str = ""
    while dec_num > 0:
        remainder = dec_num % 16
        hex_str = hexDigits[remainder] + hex_str
        dec_num //= 16
    return hex_str
def octal_to_decimal(octal_num):
    decimal = 0
    for i,digit in enumerate(reversed(str(octal_num))):
        decimal += str_to_int(digit) * (8 ** i)
    return decimal
def decimal_to_octal(dec_num):
    if dec_num == 0:
        return "0"
    octal_str = ""
    while dec_num > 0:
        remainder = dec_num % 8
        octal_str = str(remainder) + octal_str
        dec_num //= 8
    return str_to_int(octal_str)
def base36_to_decimal(base36_str):
    base36Digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base36_str = base36_str.upper()
    decimal = 0
    for i,digit in enumerate(reversed(base36_str)):
        value = base36Digits.index(digit)
        decimal += value * (36 ** i)
    return decimal
def decimal_to_base36(dec_num):
    if dec_num == 0:
        return "0"
    base36Digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base36_str = ""
    while dec_num > 0:
        remainder = dec_num % 36
        base36_str = base36Digits[remainder] + base36_str
        dec_num //= 36
    return str_to_int(base36_str)
def duodecimal_to_decimal(duodecimal_str):
    duodecimalDigits = "0123456789AB"
    duodecimal_str = duodecimal_str.upper()
    decimal = 0
    for i,digit in enumerate(reversed(duodecimal_str)):
        value = duodecimalDigits.index(digit)
        decimal += value * (12 ** i)
    return decimal
def decimal_to_duodecimal(dec_num):
    if dec_num == 0:
        return "0"
    duodecimalDigits = "0123456789AB"
    duodecimal_str = ""
    while dec_num > 0:
        remainder = dec_num % 12
        duodecimal_str = duodecimalDigits[remainder] + duodecimal_str
        dec_num //= 12
    return str_to_int(duodecimal_str)
def base64_to_decimal(base64_str):
    base64Digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
    decimal = 0
    for i,digit in enumerate(reversed(base64_str)):
        value = base64Digits.index(digit)
        decimal += value * (64 ** i)
    return decimal
def decimal_to_base64(dec_num):
    if dec_num == 0:
        return "0"
    base64Digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
    base64_str = ""
    while dec_num > 0:
        remainder = dec_num % 64
        base64_str = base64Digits[remainder] + base64_str
        dec_num //= 64
    return str_to_int(base64_str)
def alphanumberic_to_decimal(alphanum_str):
    alphanumDigits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    decimal = 0
    for i,digit in enumerate(reversed(alphanum_str)):
        value = alphanumDigits.index(digit)
        decimal += value * (62 ** i)
    return decimal
def decimal_to_alphanumberic(dec_num):
    if dec_num == 0:
        return "0"
    alphanumDigits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    alphanum_str = ""
    while dec_num > 0:
        remainder = dec_num % 62
        alphanum_str = alphanumDigits[remainder] + alphanum_str
        dec_num //= 62
    return str_to_int(alphanum_str)
def sexagesimal_to_decimal(sexagesimal_str):
    parts = list(map(int, sexagesimal_str.split(":")))
    decimal = 0
    for i, part in enumerate(reversed(parts)):
        decimal += part * (60 ** i)
    return decimal
def decimal_to_sexagesimal(dec_num):
    if dec_num == 0:
        return "0"
    sexagesimal_str = ""
    while dec_num > 0:
        remainder = dec_num % 60
        sexagesimal_str = str(remainder) + (":" if sexagesimal_str else "") + sexagesimal_str
        dec_num //= 60
    return sexagesimal_str
def decimal_to_base90(n):
    BASE90_SYMBOLS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`"
    BASE90 = len(BASE90_SYMBOLS)
    
    if n == 0:
        return BASE90_SYMBOLS[0]
    
    result = ""
    while n > 0:
        n, rem = divmod(n, BASE90)
        result += BASE90_SYMBOLS[rem]
    return result
def base90_to_decimal(s):
    BASE90_SYMBOLS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`"
    BASE90 = len(BASE90_SYMBOLS)
    decimal_value = 0
    for char in s:
        decimal_value = decimal_value * BASE90 + BASE90_SYMBOLS.index(char)
    return decimal_value
from enum import Enum as Enum
class Base(Enum):
    BINARY = 2
    OCTAL = 8
    DECIMAL = 10
    HEXADECIMAL = 16
    BASE36 = 36
    DUODECIMAL = 12
    BASE64 = 64
    ALPHANUMERIC = 62
    SEXAGESIMAL = 60
    BASE90 = 90
def convert_base(num_str, from_base:Base, to_base:Base):
    base_conversion_functions = {
        (Base.BINARY, Base.DECIMAL): bin_to_dec,
        (Base.DECIMAL, Base.BINARY): dec_to_bin,
        (Base.HEXADECIMAL, Base.DECIMAL): hexadecimal_to_decimal,
        (Base.DECIMAL, Base.HEXADECIMAL): decimal_to_hexadecimal,
        (Base.OCTAL, Base.DECIMAL): octal_to_decimal,
        (Base.DECIMAL, Base.OCTAL): decimal_to_octal,
        (Base.BASE36, Base.DECIMAL): base36_to_decimal,
        (Base.DECIMAL, Base.BASE36): decimal_to_base36,
        (Base.DUODECIMAL, Base.DECIMAL): duodecimal_to_decimal,
        (Base.DECIMAL, Base.DUODECIMAL): decimal_to_duodecimal,
        (Base.BASE64, Base.DECIMAL): base64_to_decimal,
        (Base.DECIMAL, Base.BASE64): decimal_to_base64,
        (Base.ALPHANUMERIC, Base.DECIMAL): alphanumberic_to_decimal,
        (Base.DECIMAL, Base.ALPHANUMERIC): decimal_to_alphanumberic,
        (Base.SEXAGESIMAL, Base.DECIMAL): sexagesimal_to_decimal,
        (Base.DECIMAL, Base.SEXAGESIMAL): decimal_to_sexagesimal,
        (Base.BASE90, Base.DECIMAL): base90_to_decimal,
        (Base.DECIMAL, Base.BASE90): decimal_to_base90
    }
    
    if from_base == to_base:
        return num_str
    
    if (from_base, to_base) in base_conversion_functions:
        return str(base_conversion_functions[(from_base, to_base)](num_str))
    else:
        raise ValueError(f"Conversion from {from_base} to {to_base} is not supported.")
def palindrome_checker(num):
    num_str = str(num)
    return num_str == num_str[::-1]
def number_of_n_digit_primes(n : int):
    if n < 1:
        raise ValueError("Number of digits must be at least 1.")
    lower_bound = 10**(n-1)
    upper_bound = 10**n
    n_digit_primes = []
    for num in range(lower_bound, upper_bound + 1):
        if is_prime(num):
            n_digit_primes.append(num)
            print(num)
    return n_digit_primes