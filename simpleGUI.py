from tkinter import *
import tkinter
import tkinter.messagebox

def doThing():
    num1 = int(Entry.get(E1))
    num2 = int(Entry.get(E1))
    op = Entry.get(E3)
    if op == "+":
        ans = num1+num2
    elif op == "-":
        ans = num1-num2
    elif op == "*":
        ans = num1*num2
    elif op == "/":
        ans = num1/num2
    else:
        print("error, bad op")
        ans = "error"
    Entry.insert(E4, 0, ans)
    print(ans)


top = Tk()
L1 = Label(top, text="My calculator",).grid(row=0, column=1)
L2 = Label(top, text="Number 1",).grid(row=1, column=0)
L3 = Label(top, text="Number 2",).grid(row=2, column=0)
L4 = Label(top, text="Operator",).grid(row=3, column=0)
L4 = Label(top, text="Answer",).grid(row=4, column=0)
E1 = Entry(top, bd=5)
E1.grid(row=1, column=1)
E2 = Entry(top, bd=5)
E2.grid(row=2, column=1)
E3 = Entry(top, bd=5)
E3.grid(row=3, column=1)
E4 = Entry(top, bd=5)
E4.grid(row=4, column=1)
B = Button(top, text="Submit", command=doThing).grid(row=5, column=1,)

top.mainloop()
