import tkinter
from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")

root.configure(bg="#000000")
root.resizable(0,0)

equation=""

def show(value): 
    global equation
    equation+=value
    Label_result.config(text=equation)

def clear():
    global equation
    equation=""
    Label_result.config(text=equation)

def calculate():
    global equation
    result =""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    Label_result.config(text=result)



Label_result=Label(root,width=25,height=2,text="",font=("arial",30))
Label_result.pack()

Button(root,text="C",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#243630",command=lambda: clear()).place(x=10,y=100)
Button(root,text="/",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda:show("/")).place(x=150,y=100)
Button(root,text="%",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show("%")).place(x=290,y=100)
Button(root,text="*",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show("*")).place(x=430,y=100)

Button(root,text="7",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show("7")).place(x=10,y=200)
Button(root,text="8",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show("8")).place(x=150,y=200)
Button(root,text="9",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show("9")).place(x=290,y=200)
Button(root,text="-",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show("-")).place(x=430,y=200)

Button(root,text="4",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show("4")).place(x=10,y=300)
Button(root,text="5",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show("5")).place(x=150,y=300)
Button(root,text="6",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show("6")).place(x=290,y=300)
Button(root,text="+",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show("+")).place(x=430,y=300)

Button(root,text="1",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show("1")).place(x=10,y=400)
Button(root,text="2",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show("2")).place(x=150,y=400)
Button(root,text="3",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show("3")).place(x=290,y=400)
Button(root,text="0",width=11,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show("0")).place(x=10,y=500)

Button(root,text=".",width=5,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3b6154",command=lambda: show(".")).place(x=290,y=500)
Button(root,text="=",width=5,height=3, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#0a2e23",command=lambda: calculate()).place(x=430,y=400)



root.mainloop()
