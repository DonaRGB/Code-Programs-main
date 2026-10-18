class btn:
    def __init__(self,i):
        self.data = i
        self.l = None
        self.r = None
    def insert(self,x):
        if x < self.data:
            if self.l is None:
                self.l = btn(x)
                print(f"Inserted {x} to the left of {self.data}.")
            else:
                self.l.insert(x)
        elif x > self.data:
            if self.r is None:
                self.r = btn(x)
                print(f"Inserted {x} to the right of {self.data}.")
            else:
                self.r.insert(x)
        else:
            print(f"Value {x} already exists in the tree.")
    def search(self,k):
        if self.data == k:
            print(f"Found {k}!")
            return True
        elif k < self.data:
            if self.l is not None:
                return self.l.search(k)
            else:
                print(f"{k} not found in tree.")
                return False
        elif k > self.data:
            if self.r is not None:
                return self.r.search(k)
            else:
                print(f"{k} not found in tree.")
                return False
root = btn(13)
root.insert(2)
root.insert(24)
root.insert(23)
root.insert(9)
root.search(2)
root.search(15)
root.search(24)
root.search(3)