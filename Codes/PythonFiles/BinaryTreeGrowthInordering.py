from binarytree import Node as Node
root = Node(1)
root.l = Node(2)
root.r = Node(3)
root.l.l = Node(4)
root.l.r = Node(5)
root.r.l = Node(5)
root.r.r = Node(6)
print("Binary Tree Structure :\n",root)
def in_order_traversal(node):
    if node:
        in_order_traversal(node.l)
        print(node.value,end = " ")
        in_order_traversal(node.r)
def pre_order_traversal(node):
    if node:
        print(node.value,end = " ")
        pre_order_traversal(node.l)
        pre_order_traversal(node.r)
def post_order_traversal(node):
    if node:
        post_order_traversal(node.l)
        post_order_traversal(node.r)
        print(node.value,end = " ")
print("\nIn-order traversal :")
in_order_traversal(root)
print("\nPre-order traversal :")
pre_order_traversal(root)
print("\nPost-order traversal :")
post_order_traversal(root)