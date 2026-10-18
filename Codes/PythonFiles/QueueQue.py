class Queue:
    def __init__(self,n):
        self.size = n
        self.arr = [0] * n
        self.front = -1
        self.rear = -1
    def enqueue(self,i):
        if self.rear == self.size - 1:
            print("Overflow!",end = " ")
            print("\n",end = " ")
            return
        else:
            if self.front == -1 and self.rear == -1:
                self.front = 0
                self.rear = 0
            else:
                self.rear += 1
        self.arr[self.rear] = i
        print("Element inserted successfully!")
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Underflow!",end = " ")
            print("\n",end = " ")
            return
        else:
            x = self.arr[self.front]
            print("Element deleted from queue :",end = " ")
            print(x,end = " ")
            print("\n",end = " ")
            if self.rear == self.front:
                self.rear = -1
                self.front = -1
            else:
                self.front += 1
    def display(self):
        if self.front == -1:
            print("Queue is empty!",end = " ")
            print("\n",end = " ")
            return
        else:
            print("Queue :",end = " ")
            p = self.front
            while p <= self.rear:
                print(self.arr[p],end = " ")
                print(" ",end = " ")
                p += 1
            print("\n",end = " ")
    def display_front(self):
        if self.front == -1:
            print("Queue is empty!",end = " ")
            print("\n",end = " ")
            return
        else:
            print("The front element :",end = " ")
            print(self.arr[self.front],end = " ")
            print("\n",end = " ")
q = Queue(10)
c = None
print("1. Insert element to queue (enqueue)\n2. Remove element from queue (dequeue)\n3. Display the front element\n4. Display the queue\n5. Exit\n")
while True:
    c = int(input("Enter your choice : "))
    if c == 1:
        i = int(input("Enter an element : "))
        q.enqueue(i)
    elif c == 2:
        q.dequeue()
    elif c == 3:
        q.display_front()
    elif c == 4:
        q.display()
    elif c == 5:
        print("Exit\n")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5")