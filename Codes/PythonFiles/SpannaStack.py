def calculateSpan(S,price):
    n = len(price)
    st = [0]
    S[0] = 1
    for i in range(1,n):
        while len(st) > 0 and price[st[-1]] <= price[i]:
            st.pop()
        S[i] = i + 1 if len(st) == 0 else (i-st[-1])
        st.append(i)
def printArr(a):
    for i in a:
        print(i,end = " ")
price = [32,43,34,53,97,34,74]
S = [0] * len(price)
calculateSpan(S,price)
printArr(S)