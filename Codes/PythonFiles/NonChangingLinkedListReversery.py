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
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def reverse(self):
        if self.head == None:
            print("List is empty!")
            return
        v = []
        t = self.head
        while t:
            v.append(t.data)
            t = t.next
        t = self.head
        i = len(v) - 1
        while t:
            t.data = v[i]
            i -= 1
            t = t.next
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