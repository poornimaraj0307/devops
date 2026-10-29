from tkinter import *

def add():
    a = e1.get()
    b = e2.get()
    c = int(a) + int(b)
    e3.delete(0, END)
    e3.insert(0, str(c))

def sub():
    a = e1.get()
    b = e2.get()
    c = int(a) - int(b)
    e3.delete(0, END)
    e3.insert(0, str(c))

def mul():
    a = e1.get()
    b = e2.get()
    c = int(a) * int(b)
    e3.delete(0, END)
    e3.insert(0, str(c))

def div():
    a = e1.get()
    b = e2.get()
    try:
        c = int(a) / int(b)
        e3.delete(0, END)
        e3.insert(0, str(c))
    except ZeroDivisionError:
        e3.delete(0, END)
        e3.insert(0, "Cannot divide by 0")

root = Tk()
root.title("Operation")
root.geometry("300x300")

l1 = Label(root, text="Number 1")
l1.pack()

e1 = Entry(root)
e1.pack()

l2 = Label(root, text="Number 2")
l2.pack()

e2 = Entry(root)
e2.pack()

l3 = Label(root, text="Result")
l3.pack()

e3 = Entry(root)
e3.pack()

b1 = Button(root, text="Add", command=add)
b1.pack()

b2 = Button(root, text="Subtract", command=sub)
b2.pack()

b3 = Button(root, text="Multiply", command=mul)
b3.pack()

b4 = Button(root, text="Divide", command=div)
b4.pack()

root.mainloop()
