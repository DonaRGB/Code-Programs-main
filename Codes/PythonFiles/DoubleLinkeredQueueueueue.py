class GFG:
    class Node:
        data = 0
        prev = None
        next = None
        @staticmethod
        def getNode(i):
            nN = GFG.Node()
            nN.data = i
            nN.prev = None
            nN.next = None
            return nN
    class DLQ:
        f = None
        r = None
        n = 0
        def __init__(self):
            self.f = None
            self.r = None
            self.n = 0
        def isEmpty(self):
            return self.f is None
        def size(self):
            return self.n
        def inf(self,i):
            nN = GFG.Node.getNode(i)
            if nN is None:
                print("Overflow!",end = "\n")
            else:
                if self.f == None:
                    self.f = self.r = nN
                else:
                    nN.next = self.f
                    self.f.prev = nN
                    self.f = nN
                self.n += 1
        def inr(self,i):
            nN = GFG.Node.getNode(i)
            if nN is None:
                print("Overflow!",end = "\n")
            else:
                if self.r == None:
                    self.f = self.r = nN
                else:
                    nN.prev = self.r
                    self.r.next = nN
                    self.r = nN
                self.n += 1
        def delf(self):
            if self.isEmpty():
                print("Underflow!",end = "\n")
            else:
                t = self.f
                self.f = self.f.next
                if self.f is None:
                    self.r = None
                else:
                    self.f.prev = None
                self.n -= 1
        def delr(self):
            if self.isEmpty():
                print("Underflow!",end = "\n")
            else:
                t = self.r
                self.r = self.r.prev
                if self.r is None:
                    self.f = None
                else:
                    self.r.next = None
                self.n -= 1
        def front(self):
            if self.isEmpty():
                return -1
            return self.f.data
        def rear(self):
            if self.isEmpty():
                return -1
            return self.r.data
        def erase(self):
            self.r = None
            while self.f != None:
                t = self.f
                self.f = self.f.next
            self.n = 0
    @staticmethod
    def main(args):
        dq = GFG.DLQ()
        print("Insert \"5\" at rear end\n",end = "")
        dq.inr(5)
        print("Insert \"10\" at rear end\n",end = "")
        dq.inr(10)
        print(f"Rear end element : {dq.rear()}\n",end = "")
        dq.delr()
        print(f"After deleting, new rear end element : {dq.rear()}\n",end = "")
        print("Insert \"15\" at front end\n",end = "")
        dq.inf(15)
        print(f"Front end element : {dq.front()}\n",end = "")
        print("Size of queue :",dq.size(),"\n",end = "")
        dq.delf()
        print(f"After deleting, new front end element : {dq.front()}\n",end = "")
GFG.main([])