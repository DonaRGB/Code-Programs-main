class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SinglyLL:
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
    def delete_beg(self):
        if self.head != None:
            t = self.head
            self.head = self.head.next
            t = None
    def delete_end(self):
        if self.head != None:
            if self.head.next == None:
                self.head = None
            else:
                t = self.head
                while t.next.next:
                    t = t.next
                t.next = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev
l = SinglyLL()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
print("Original List :")
l.display()
l.reverse()
print("Reversed List :")
l.display()