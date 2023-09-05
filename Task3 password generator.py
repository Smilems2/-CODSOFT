from tkinter import*
from random import randint

root=Tk()
root.title("Password Generator")
root.geometry("500x300")
root.resizable(0,0)
root.configure(bg="#5b3244")

my_password=chr(randint(33,126))

def new_rand():
    pw_entry.delete(0,END)
    pw_length=int(my_entry.get())
    my_password=''
    for x in range(pw_length):
        my_password+=chr(randint(33,126))
    pw_entry.insert(0, my_password)



lf=LabelFrame(root,text="Number of characters:",fg="black")
lf.pack(pady=20)

my_entry=Entry(lf,font=("arial",24),bg="#dec3c1")
my_entry.pack(pady=20,padx=20)

pw_entry=Entry(root,text='',font=("arial",24),bd=0,bg="#dec3c1")
pw_entry.pack(pady=20)

my_frame=Frame(root)
my_frame.pack(pady=20)

my_button=Button(my_frame,text="Generate strong password",command=new_rand,bg="#dec3c1",fg="black")
my_button.grid(row=0,column=0,padx=10)




root.mainloop()