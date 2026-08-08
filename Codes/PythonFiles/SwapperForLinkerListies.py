class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SinglyLL:
    def __init__(self):
        self.head = None
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
    def swap(self,n1,n2):
        prevNode1 = None
        prevNode2 = None
        node1 = self.head
        node2 = self.head
        if self.head == None:
            return
        if n1 == n2:
            return
        while node1 != None and node1.data != n1:
            prevNode1 = node1
            node1 = node1.next
        while node2 != None and node2 != n2:
            prevNode2 = node2
            node2 = node2.next
        if node1 != None and node2 != None:
            if prevNode1 != None:
                prevNode1.next == node2
            else:
                self.head = node2
            if prevNode2 != None:
                prevNode2.next = node1
            else:
                self.head = node1
            t = node1.next
            node1.next = node2.next
            node2.next = t
        else:
            print("Swapping is not possible!")
    def display(self):
        if self.head == None:
            print("List is empty")
        else:
            t = self.head
            while t:
                print(t.data,"-->",end = " ")
                t = t.next
            print("None")
l = SinglyLL()
n = Node(10)
l.head =  n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
n3 = Node(40)
n2.next = n3
l.display()
print(end = "\n")
l.swap(10,30)
l.display()