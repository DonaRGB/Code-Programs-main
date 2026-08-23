x = [[2,3,4],
    [3,4,5],
    [4,5,6]]
a = [[0]*3]*3
for i in range(len(x)):
    for j in range(len(x[0])):
        a[i][j] = x[j][i]
for r in a:
    print(r)