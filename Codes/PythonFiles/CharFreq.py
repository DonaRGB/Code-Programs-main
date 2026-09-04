def freq_letters_dic(s):
    s = s.replace(" ","").lower()
    d = {}
    for i in s:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    return d
def freq_letters_naive(s):
    s = s.replace(" ","").lower()
    d = {}
    for i in s:
        d[i] = s.count(i)
    return d
s = str(input("Enter string : "))
print("String :",s)
print("Frequency of letters in the said string (dictionary method): " + str(freq_letters_dic(s)))
print("Frequency of letters in the said string (naive method) : " + str(freq_letters_naive(s)))