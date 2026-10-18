class btn:
    def __init__(self,i):
        self.data = i
        self.lc = None
        self.rc = None
def insert_node(root,nv):
    if root is None:
        return btn(nv)
    if nv < root.data:
        root.lc = insert_node(root.lc,nv)
    elif nv > root.data:
        root.rc = insert_node(root.rc,nv)
    else:
        print(f"Value {nv} already exists in the tree.")
    return root
def delete_tree(root):
    if root:
        delete_tree(root.lc)
        root.lc = None
        delete_tree(root.rc)
        root.rc = None
        print(f"Deleteing Node : {root.data}")
        root.data = None
root = insert_node(None,15)
insert_node(root,34)
insert_node(root,3)
insert_node(root,4)
insert_node(root,5)
insert_node(root,36)
insert_node(root,86)
print("Deleting all elements in binary tree.")
delete_tree(root)
root = None