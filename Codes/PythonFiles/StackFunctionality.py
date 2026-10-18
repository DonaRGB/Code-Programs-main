class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return True if self.head is None else False
    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            n = Node(data)
            n.next = self.head
            self.head = n
    def topElement(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
    def pop(self):
        if self.isEmpty():
            return None
        else:
            p = self.head
            self.head = self.head.next
            p.next = None
            return p.data
s = Stack()
s.push(5)
s.push(4)
s.push(0)
s.push(8)
s.push(6)
print("The element at the top :\n",s.topElement())
print("The element popped :\n",s.pop())
print("The element at the top :\n",s.topElement())
print("The element popped :\n",s.pop())
print("The element at the top :\n",s.topElement())
print("The element popped :\n",s.pop())