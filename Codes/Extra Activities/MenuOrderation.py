import tkinter as tk
from tkinter import messagebox as mb
menu = {
    "Pizza":1.5,
    "Burger":1.75,
    "Pasta":1,
    "Coffee":3,
    "Ice Cream":5
}
def calculate_bill():
    total = 0
    bill_details = "---------- Bill ----------\n"
    tax_rate = 5/100
    for item,price in menu.items():
        qty = entries[item].get()
        if qty.is_digit() and int(qty) > 0:
            qty = int(qty)
            cost = qty * price
            total += cost
            bill_details += f"{item} x {qty} = ${cost:.2f}\n"
    tax = total * tax_rate
    grand_total = total + tax
    bill_details += f"\nSubtotal : ${total:.2f}"
    bill_details += f"\nTax ({tax_rate * 100}%) : ${tax:.2f}"
    bill_details += f"\nTotal : ${grand_total:.2f}"
    mb.showinfo("Bill",bill_details)
root = tk.Tk()
root.title("Restaurant Billing App")
entries = {}
row = 0
for item,price in menu.items():
    tk.Label(root,text = f"{item} $({price:.2f})").grid(row = row,column = 0,padx = 10,pady = 5,sticky = "w")
    entry = tk.Entry(root)
    entry.grid(row = row, column = 1, padx = 10, pady = 5)
    entries[item] = entry
    row += 1
tk.Button(root,text = "Generate Bill",command= calculate_bill,bg = "green",fg = "white").grid(row = row, columnspan = 2, pady = 10)
root.mainloop()