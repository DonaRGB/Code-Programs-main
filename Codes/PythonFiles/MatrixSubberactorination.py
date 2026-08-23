def subtract_matrices(a,b):
    if len(a) != len(b):
        raise Exception("The sizes of the matrices are not the same!")
    if len(a[0]) != len(b[0]):
        raise Exception("The sizes of the matrices are not the same!")
    ans = [[0] * len(b[0])] * len(a)
    for i in range(len(a)):
        for j in range(len(b[i])):
            ans[i][j] = a[i][j] - b[i][j]
    return ans
def print_matrix(m):
    for r in m:
        for c in r:
            print(c,end = " ")
        print("\n")
x = [[2,3],
    [4,5]]
y = [[4,2],
    [5,9]]
a = subtract_matrices(x,y)
print("Original Matrices :")
print("X :")
print_matrix(x)
print("Y :")
print_matrix(y)
print("Difference of the matrices :")
print_matrix(a)