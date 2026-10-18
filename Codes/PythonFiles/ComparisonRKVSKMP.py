def rabin_karp_al(text,pattern):
    m = len(pattern)
    n = len(text)
    d = 10
    q = 13
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0
    for i in range(m-1):
        h = (h*d) % q
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            j += 1
            if j == m:
                print("Pattern is found at position :",i+1)
        if i < n-m:
            t = (d*(t - ord(text[i])*h)) + ord(text[i+m]) % q
            if t < 0:
                t += q
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
print("Rabin-Karp Search Results :")
rabin_karp_al(text,pattern)
print("KMP Search Results :")
kmp_search(text,pattern)