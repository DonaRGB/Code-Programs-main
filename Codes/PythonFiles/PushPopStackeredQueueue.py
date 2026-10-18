from _collections import deque as dequeue
class Stack:
    def __init__(self):
        self.q1 = dequeue()
        self.q2 = dequeue()
    def push(self,x):
        self.q1.append(x)
    def pop(self):
        if not self.q1:
            return
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2 = self.q2,self.q1
    def top(self):
        if not self.q1:
            return
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        t = self.q1[0]
        self.q2.append(self.q1.popleft())
        self.q1,self.q2 = self.q2,self.q1
        return t
    def size(self):
        return len(self.q1)
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("Current size :",s.size())
print(s.top())
s.pop()
print(s.top())
s.pop()
print(s.top())
print("Current size :",s.size())