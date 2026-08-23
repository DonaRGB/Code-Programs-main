def multiply_matrices(a,b):
    if len(a) != len(b[0]) or len(b) != len(a[0]):
        raise Exception("Dimensions not possible to multiply!")
    ans = []
    m = []
    n = []
    if len(a) == len(b[0]):
        ans = [[0] * len(a[0])] * len(b)
        m = a
        n = b
    elif len(a[0]) == len(b):
        ans = [[0] * len(b[0])] * len(a)
        m = b
        n = a
    t = 0
    for i in range(len(n)):
        for j in range(len(m[0])):
            for k in range(len(m)):
                ans[i][j] += n[i][k] * m[k][j]
    return ans
def print_matrix(m):
    for r in m:
        for c in r:
            print(c,end = " ")
        print("\n")
x = [[8,2],
    [4,1]]
y = [[3,8],
    [9,15]]
ans = multiply_matrices(x,y)
print("Original Matrices :")
print("X :")
print_matrix(x)
print("Y :")
print_matrix(y)
print("Product of the matrices :")
print_matrix(ans)