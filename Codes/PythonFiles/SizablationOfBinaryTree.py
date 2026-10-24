class Node:
    def __init__(self,x):
        self.data = x
        self.l = None
        self.r = None
def find_size_recursive(root):
    if root is None:
        return 0
    return find_size_recursive(root.l)+find_size_recursive(root.r)+1
def find_size_iterative(root):
    if root is None:
        return 0
    c = 0
    stack = [root]
    while stack:
        n = stack.pop()
        c += 1
        if n.l is not None:
            stack.append(n.l)
        if n.r is not None:
            stack.append(n.r)
    return c
root = Node(1)
root.l = Node(2)
root.r = Node(3)
root.l.l = Node(4)
root.l.r = Node(5)
root.r.l = Node(6)
root.r.r = Node(7)
root.l.l.l = Node(8)
root.l.l.r = Node(9)
root.l.r.l = Node(10)
root.l.r.r = Node(11)
root.r.l.l = Node(12)
root.r.l.r = Node(13)
root.r.r.l = Node(14)
root.r.r.r = Node(15)
size_rec = find_size_recursive(root)
size_ite = find_size_iterative(root)
print("The size of the binary tree (recursive) is :",size_rec)
print("The size of the binary tree (iterative) is :",size_ite)