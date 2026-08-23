def sum_rows(x):
    if len(x) == 0:
        return [0]
    elif len(x[0]) == 0:
        return [0]
    sr = [0] * len(x)
    for i in range(len(x)):
        for j in range(len(x[0])):
            sr[i] += x[i][j]
    return sr
x = [[3,4,5],
    [4,5,6],
    [5,6,7]]
a = sum_rows(x)
for i in a:
    print(i,end = " ")