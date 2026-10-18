def kmp_search(text,pattern):
    m = len(pattern)
    n = len(text)
    lps = [0] * m
    j = 0
    LPSArray(pattern,m,lps)
    i = 0
    while n - i >= m - j:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            print("Found pattern at index :",i-j)
            j = lps[j-1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
def LPSArray(p,m,lps):
    l = 0
    lps[0] = 0
    i = 1
    while i < m:
        if p[i] == p[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            lps[i] = 0
            i += 1
text = "AABBCCDDEEFFGGAABBCCDD"
pattern = "AABB"
kmp_search(text,pattern)