class Node:
    def __init__(self,i):
        self.data = i
        self.next = None
class LinkedQueue:
    def __init__(self):
        self.f = self.r = None
    def isEmp(self):
        return self.f is None
    def enqueue(self,i):
        t = Node(i)
        if self.r == None:
            self.front = self.rear = t
            return
        self.r.next = t
        self.r = t
    def dequeue(self):
        if self.isEmp():
            return
        t = self.f
        self.f = t.next
        if self.f == None:
            self.r = None
    def front(self):
        return str(self.f.data if self.f != None else -1)
    def rear(self):
        return str(self.r.data if self.r != None else -1)
q = LinkedQueue()
q.enqueue(10)
q.enqueue(20)
q.dequeue()
q.dequeue()
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.dequeue()
print("Queue Front :",q.front())
print("Queue Rear :",q.rear())