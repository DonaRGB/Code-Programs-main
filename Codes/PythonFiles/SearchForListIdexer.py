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
    def search(self,data):
        if self.head == None:
            print("List is empty!")
        else:
            t = self.head
            not_found = True
            while t and not_found:
                if t.data == data:
                    not_found = False
                    print("Data found in the list")
                t = t.next
            if not_found:
                print("Data not found in the list")
                return False
    def display(self):
        t = self.head
        while t:
            print(t.data,"-->",end = " ")
            t = t.next
def ordinal_number(d:int):
    de = str(d)[-1]
    if len(str(d)) > 1 and str(d)[-2] == "1":
        return f"{d}th"
    if de == "1":
        return f"{d}st"
    elif de == "2":
        return f"{d}nd"
    elif de == "3":
        return f"{d}rd"
    else:
        return f"{d}th"

l = SinglyLL()
length = int(input("Enter the length of the list : "))
n = Node(int(input("\nEnter the 1st value : ")))
l.head = n
for i in range(2,length+1):
    n1 = Node(int(input(f"Enter the {ordinal_number(i)} value : ")))
    n.next = n1
    n = n1
print("\n")
l.display()
print("\n")
s = int(input("Enter the value to be searched : "))
print(end = "\n")
l.search(s)