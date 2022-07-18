import tkinter
from tkinter import *

val = ""
def btnClick(number):
    global val
    val = val + str(number)
    data.set(val)

def btnClear():
    global val
    val = ""
    data.set("")

def btnEquals():
    global val
    result = str(eval(val))
    data.set(result)

root = tkinter.Tk()
root.geometry("250x400")
root.resizable(0,0)
root.title("Calculater")

data = StringVar()
lable = Label(root, text="calci",anchor=SE,textvariable=data,font=("Arial",30),bg="#000000",fg="#ffffff")
lable.pack(expand=True, fill="both")

btnrow1 = Frame(root,bg="#000000")
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")

# \\\\\\\\\\\\\\\ FIRST ROW \\\\\\\\\\\\

btn1 =Button(btnrow1, text="1",font=("Arial",22), relief=GROOVE,border=0,command=lambda : btnClick(1))
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 =Button(btnrow1, text="2",font=("Arial",22), relief=GROOVE,border=0,command=lambda : btnClick(2))
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 =Button(btnrow1, text="3",font=("Arial",22), relief=GROOVE,border=0,command=lambda : btnClick(3))
btn3.pack(side=LEFT, expand=True, fill="both")

btnplus =Button(btnrow1, text="+",font=("Arial",22), relief=GROOVE,border=0,command=lambda : btnClick("+"))
btnplus.pack(side=LEFT, expand=True, fill="both")

# \\\\\\\\\\\\ SECONF ROW \\\\\\\\\\\

btn4=Button(btnrow2, text="4",font=("Arial",22), relief=GROOVE,border=0,command=lambda : btnClick(4))
btn4.pack(side=LEFT, expand=True, fill="both")

btn5 =Button(btnrow2, text="5",font=("Arial",22), relief=GROOVE,border=0,command=lambda : btnClick(5))
btn5.pack(side=LEFT, expand=True, fill="both")

btn6 =Button(btnrow2, text="6",font=("Arial",22), relief=GROOVE,border=0,command=lambda : btnClick(6))
btn6.pack(side=LEFT, expand=True, fill="both")

btnsub =Button(btnrow2, text="-",font=("Arial",22), relief=GROOVE,border=0,command=lambda : btnClick("-"))
btnsub.pack(side=LEFT, expand=True, fill="both")

# \\\\\\\\\\\\ TRIRD ROW \\\\\\\\\\\\\\

btn7 =Button(btnrow3, text="7",font=("Arial",22), relief=GROOVE,border=0,command=lambda : btnClick(7))
btn7.pack(side=LEFT, expand=True, fill="both")

btn8 =Button(btnrow3, text="8",font=("Arial",22), relief=GROOVE,border=0,command=lambda : btnClick(8))
btn8.pack(side=LEFT, expand=True, fill="both")

btn9 =Button(btnrow3, text="9",font=("Arial",22), relief=GROOVE,border=0,command=lambda : btnClick(9))
btn9.pack(side=LEFT, expand=True, fill="both")

btnmul =Button(btnrow3, text="*",font=("Arial",22), relief=GROOVE,border=0,command=lambda : btnClick("*"))
btnmul.pack(side=LEFT, expand=True, fill="both")

# \\\\\\\\\\\\\\\ FOURTH ROW \\\\\\\\\\\\\

btnclr =Button(btnrow4, text="C",font=("Arial",22), relief=GROOVE,border=0,command=btnClear)
btnclr.pack(side=LEFT, expand=True, fill="both")

btn0 =Button(btnrow4, text="0",font=("Arial",22), relief=GROOVE,border=0,command=lambda : btnClick(0))
btn0.pack(side=LEFT, expand=True, fill="both")

btnequal =Button(btnrow4, text="=",font=("Arial",22), relief=GROOVE,border=0,command= btnEquals)
btnequal.pack(side=LEFT, expand=True, fill="both")

btndiv =Button(btnrow4, text="/",font=("Arial",22), relief=GROOVE,border=0,command=lambda : btnClick("/"))
btndiv.pack(side=LEFT, expand=True, fill="both")





root.mainloop()