keys = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def printCombinations(com,cur,o,n):
    if cur == n:
        print(*o,sep = ",")
        return
    for i in range(len(keys[com[cur]])):
        o.append(key[com[cur]][i])
        printCombinations(com,cur+1,o,n)
        o.pop()
        if com[cur] == 0 or com[cur] == 1:
            return
combination = [4,3,4]
n = len(combination)
printCombinations(combination,0,[],n)