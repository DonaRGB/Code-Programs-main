def factors(n:int):
    if type(n) != int or n < 1:
        raise ValueError("You can only factor whole numbers!")
    return [i for i in range(1,n + 1) if n % i == 0]
def is_prime(n:int):
    if type(n) != int:
        return False
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_factors(n:int):
    if type(n) != int or n < 1:
        raise ValueError("You can only factor whole numbers!")
    return [i for i in range(2, n + 1) if n % i == 0 and is_prime(i)]
def ordinal_number_converter(d:int):
    if type(d) != int:
        raise ValueError("You can only convert whole numbers to ordinal form!")
    de = str(d)[-1]
    if len(str(d)) > 1 and str(d)[-2] == "1":
        return f"{d}th"
    if de == "1":
        return f"{d}st"
    elif de == "2":
        return f"{d}nd"
    elif de == "3":
        return f"{d}rd"
    else:
        return f"{d}th"
def factor_pairs(n:int):
    if type(n) != int or n < 1:
        raise ValueError("You can only factor whole numbers!")
    return [(i, n // i) for i in range(1, int(n**0.5) + 1) if n % i == 0]
