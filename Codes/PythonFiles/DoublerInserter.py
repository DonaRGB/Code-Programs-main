class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLL:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head == None:
            print("List is empty!")
        else:
            t = self.head
            while t:
                print(t.data,"-->",end = " ")
                t = t.next
            print("None")
    def insert_beg(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    def insert_end(self,data):
        ne = Node(data)
        t = self.head
        while t.next:
            t = t.next
        t.next = ne
        ne.prev = t

l = DoublyLL()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.prev = n
n1.next = n2
n3 = Node(40)
n2.prev = n1
n2.next = n3
n3.prev = n2
l.display()
print(end = "\n")
l.insert_beg(100)
l.display()
print(end = "\n")
l.insert_end(100)
l.display()