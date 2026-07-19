import tkinter as tk
import time as t
class MergeSortVisualizer:
    def __init__(self,master,arr):
        self.master = master
        self.arr = arr
        self.canvas = tk.Canvas(master,width = 600,height = 400,bg = "white")
        self.canvas.pack()
        self.bar_width = 600 // len(arr)
        self.draw_array(arr,"Initial Array")
        self.master.update()
        self.merge_sort(arr,0,len(arr) - 1)
    def draw_array(self,arr,title,highlight = []):
        self.canvas.delete("all")
        self.canvas.create_text(300,20,text = title,font = ("Arial",14))
        for i,v in enumerate(arr):
            x0 = i * self.bar_width
            y0 = 400 - v * 5
            x1 = (i+1) * self.bar_width
            y1 = 400
            color = "skyblue" if i not in highlight else "lightgreen"
            self.canvas.create_rectangle(x0,y0,x1,y1,fill = color)
            self.canvas.create_text(x0 + 20,y0 - 10,text = str(v),font = ("Arial",10))
        self.master.update()
        t.sleep(0.8)
    def merge_sort(self,arr,l,r):
        if l < r:
            m = (l + r) // 2
            self.draw_array(arr,f"Splitting : {arr[l:r+1]}")
            self.merge_sort(arr,l,m)
            self.merge_sort(arr,m+1,r)
            self.merge(arr,l,m,r)
    def merge(self,arr,left,mid,right):
        L = arr[left:mid+1]
        R = arr[mid+1:right+1]
        i = j = 0
        k = left
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = L[j]
                j += 1
            k += 1
            self.draw_array(arr,f"Merging : {arr[left:right+1]}",highlight = list(range(left,right+1)))
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            self.draw_array(arr,f"Merging Leftovers : {arr[left:right+1]}",highlight = list(range(left,right+1)))
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            self.draw_array(arr,f"Merging Leftovers : {arr[left:right+1]}",highlight = list(range(left,right+1)))
root = tk.Tk()
root.title("Merge Sort Visualization")
from random import randint as ri
a = [ri(1,100) for _ in range(7)]
viz = MergeSortVisualizer(root,a)
root.mainloop()