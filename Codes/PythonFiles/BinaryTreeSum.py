class Node:
    def __init__(self,x):
        self.key = x
        self.l = None
        self.r = None
def sum_tree_recursive(root):
    if root is None:
        return 0
    return sum_tree_recursive(root.l) + sum_tree_recursive(root.r) + root.key
root = Node(10)
root.l = Node(20)
root.r = Node(30)
root.l.l = Node(40)
root.l.r = Node(50)
root.r.l = Node(60)
root.r.r = Node(70)
t_sum = sum_tree_recursive(root)
print("The sum of all nodes is :",t_sum)