def sum_columns(x):
    if len(x) == 0:
        return [0]
    elif len(x[0]) == 0:
        return [0]
    sc = [0] * len(x[0])
    for i in range(x):
        for j in range(x[0]):
            sc[j] += x[i][j]
    return sc
x = [[3,4,5],
    [4,5,6],
    [5,6,7]]
a = sum_columns(x)
for i in a:
    print(i,end = " ")