def freq_letters(s):
    s = s.replace(" ","").lower()
    d = {}
    for i in s:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    return d
def if_anagram(s1,s2):
    if freq_letters(s1) == freq_letters(s2):
        return True
    return False

s1 = str(input("Enter first string : "))
s2 = str(input("Enter second string : "))
r = if_anagram(s1,s2)
if r:
    print(f"\"{s1}\" and \"{s2}\" are anagrams!")
else:
    print(f"\"{s1}\" and \"{s2}\" are not anagrams!")