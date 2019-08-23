from tkinter import *
root=Tk()
root.title("Calculator")
temp=""
equation=StringVar()
equation.set("Enter your expression:")
calculation=Label(root,textvariable=equation)
calculation.grid(columnspan=3)

def press(num):
    global temp
    temp=temp+str(num)
    equation.set(temp)

def EqualPress():
    global temp
    total=str(eval(temp))
    equation.set(total)
    temp=""

def clear():
    global temp
    temp=""
    equation.set("")


b0=Button(root,text="0",command=lambda:press(0))
b0.grid(row=4,column=1)
b1=Button(root,text="1",fg="dark green",command=lambda:press(1))
b1.grid(row=1,column=0)
b2=Button(root,text="2",fg="dark green",command=lambda:press(2))
b2.grid(row=1,column=1)
b3=Button(root,text="3",fg="dark green",command=lambda:press(3))
b3.grid(row=1,column=2)
b4=Button(root,text="4",fg="dark green",command=lambda:press(4))
b4.grid(row=2,column=0)
b5=Button(root,text="5",fg="dark green",command=lambda:press(5))
b5.grid(row=2,column=1)
b6=Button(root,text="6",fg="dark green",command=lambda:press(6))
b6.grid(row=2,column=2)
b7=Button(root,text="7",fg="dark green",command=lambda:press(7))
b7.grid(row=3,column=0)
b8=Button(root,text="8",fg="dark green",command=lambda:press(8))
b8.grid(row=3,column=1)
b9=Button(root,text="9",fg="dark green",command=lambda:press(9))
b9.grid(row=3,column=2)
Plus=Button(root,text="+",fg="orange",command=lambda:press("+"))
Plus.grid(row=1,column=3)
Minus=Button(root,text="-",fg="orange",command=lambda:press("-"))
Minus.grid(row=2,column=3)
Multiply=Button(root,text="*",fg="orange",command=lambda:press("*"))
Multiply.grid(row=3,column=3)
Divide=Button(root,text="/",fg="orange",command=lambda:press("/"))
Divide.grid(row=4,column=3)
Equal=Button(root,text="=",fg="red",command=EqualPress)
Equal.grid(row=4,column=2)
Clear=Button(root,text="C",fg="brown",bg="light blue",command=clear)
Clear.grid(row=4,column=0)

root.mainloop()






