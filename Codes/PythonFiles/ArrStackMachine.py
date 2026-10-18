from sys import maxsize as mxs
def create_stack():
    return []
def isEmptyS(stack):
    return len(stack) == 0
def pushS(stack,i):
    stack.append(i)
    print(i,"pushed to stack.")
def popS(stack):
    if isEmptyS(stack):
        return str(-mxs - 1)
    return stack.pop()
def peekS(stack):
    if isEmptyS(stack):
        return str(-mxs - 1)
    return stack[len(stack) - 1]

s = create_stack()
pushS(s,"10")
pushS(s,"20")
pushS(s,"30")
print(popS(s),"popped from stack.")