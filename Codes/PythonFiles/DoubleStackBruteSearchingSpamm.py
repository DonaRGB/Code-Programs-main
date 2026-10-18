import math
class DoubleStack:
    def __init__(self,n):
        self.size = n
        self.arr = [None] * n
        self.top1 = n//2 + 1
        self.top2 = n//2
    def push1(self,i):
        if self.top1 > 0:
            self.top1 -= 1
            self.arr[self.top1] = i
        else:
            print("Stack Overflow!")
            exit(1)
    def push2(self,i):
        if self.top2 < self.size - 1:
            self.top2 += 1
            self.arr[self.top2] = i
        else:
            print("Stack Overflow!")
            exit(1)
    def pop1(self):
        if self.top1 <= self.size//2:
            x = self.arr[self.top1]
            self.top1 += 1
            return x
        else:
            print("Stack Underflow!")
            exit(1)
    def pop2(self):
        if self.top2 >= self.size//2 + 1:
            x = self.arr[self.top2]
            self.top2 -= 1
            return x
        else:
            print("Stack Underflow!")
            exit(1)

ts = DoubleStack(5)
ts.push1(5)
ts.push2(10)
ts.push2(10)
ts.push1(13)
ts.push2(6)

print("Popped element from stack 1 :",ts.pop1())
ts.push2(12)
print("Popped element from stack 2 :",ts.pop2())