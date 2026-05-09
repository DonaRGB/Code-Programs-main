def reverseNum(n):
    if num > 0:
        l = n%10
        if n//10 > 0:
            c = reverseNum((int)(num//10))
            return l*pow(10,len(str(c))) + c
        return n
n = int(input("Enter a number to reverse : "))
print("The reversed number :",reverseNum(n))