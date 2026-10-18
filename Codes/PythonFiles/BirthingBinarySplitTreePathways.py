class Node:
    def __init__(self,i):
        self.l = None
        self.r = None
        self.data = i
    def insert(self,x):
        if x < self.data:
            if self.l is None:
                self.l = Node(x)
                print(f"Inserted {x} to the left of {self.data}.")
            else:
                self.l.insert(x)
        elif x > self.data:
            if self.r is None:
                self.r = Node(x)
                print(f"Inserted {x} to the right of {self.data}.")
            else:
                self.r.insert(x)
        else:
            print(f"Value {x} already exists in the tree.")
    def print_tree(self):
        if self.l:
            self.l.print_tree()
        print(self.data,end = " ")
        if self.r:
            self.r.print_tree()

root = Node(12)
root.insert(6)
root.insert(4)
root.insert(15)
root.print_tree()