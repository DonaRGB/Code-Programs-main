class Node:
    def __init__(self,x):
        self.data = x
        self.l = None
        self.r = None
def max_depth(root):
    if root is None:
        return 0
    ld = max_depth(root.l)
    rd = max_depth(root.r)
    return max(ld,rd)+1
root = Node(1)
root.l = Node(2)
root.r = Node(3)
root.l.l = Node(4)
root.l.r = Node(5)
root.r.l = Node(6)
root.r.r = Node(7)
height = max_depth(root)
print("Height of tree :",height)