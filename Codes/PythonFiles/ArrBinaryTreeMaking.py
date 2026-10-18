tree = [None] * 10
def ensure_capacity(i):
    if i >= len(tree):
        new_size = max(i+1,len(tree)*2)
        tree.extend([None]*(new_size - len(tree)))
def root(key):
    if tree[0] is not None:
        print("Tree already has a root")
    else:
        tree[0] = key
def set_left(key,p):
    ci = (p*2)+1
    if p >= len(tree) or tree[p] is None:
        print(f"Can\'t set left child at index {ci}, no parent found at index {p}.")
    else:
        ensure_capacity(ci)
        tree[ci] = key
def set_right(key,p):
    ci = (p*2)+2
    if p >= len(tree) or tree[p] is None:
        print(f"Can\'t set right child at index {ci}, no parent found at index {p}.")
    else:
        ensure_capacity(ci)
        tree[ci] = key
def print_tree():
    for i,v in enumerate(tree):
        if v is not None:
            print(f"{v} ",end = "")
        else:
            print("- ",end = "")
    print()
root("A")
set_left("B",0)
set_right("C",0)
set_left("D",1)
set_right("E",1)
set_left("F",2)
set_right("G",2)
set_left("H",3)
set_right("I",3)
print_tree()
def print_tree_visual(index,indent = 0):
    if index < len(tree) and tree[index] is not None:
        print_tree_visual((index*2)+2,indent + 4)
        print(" "*indent + str(tree[index]))
        print_tree_visual((index*2)+1,indent + 4)
print("Visual representation of the binary tree:")
print_tree_visual(0)