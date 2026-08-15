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
                print(t.data,"<->",end = " ")
                t = t.next
            print("None")
    def insert_by_index(self,data,index):
        n = Node(data)
        if index == 0:
            n.next = self.head
            if self.head != None:
                self.head.prev = n
            self.head = n
        else:
            t = self.head
            for _ in range(index-1):
                if t is None:
                    return
                t = t.next
            if t is None:
                return
            n.next = t.next
            n.prev = t
            if t.next != None:
                t.next.prev = n
            t.next = n
l = DoublyLL()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n1.prev = n
n2 = Node(30)
n1.prev = n
n1.next = n2
n3 = Node(40)
n2.prev = n1
n2.next = n3
n3.prev = n2
l.display()
print(end = "\n")
l.insert_by_index(25, 2)
l.display()
print(end = "\n")