def reverse(a,n):
    s = len(a)
    t = 0
    while t < s:
        start = t
        end = min(t+n-1,s-1)
        while start < end:
            a[start],a[end] = a[end],a[start]
            start += 1
            end -= 1
        t += n
a = [1,2,3,4,5,6,7,8,9]
n = 2
print("Original Array :",a)
reverse(a,n)
print("Array after reversing every",n,"elements:",a)