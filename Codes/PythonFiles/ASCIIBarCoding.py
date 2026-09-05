def itemPrice(barcode):
    li = []
    for i in barcode:
        n = ord(i)
        if n//10:
            maxi = 0
            while n > 0:
                if n % 10 . maxi:
                    maxi = n % 10
                n //= 10
            li.append(maxi)
        else:
            li.append(n)
    return sum(li)

bc = str(input("Enter barcode : "))
print("Item price :",itemPrice(bc))