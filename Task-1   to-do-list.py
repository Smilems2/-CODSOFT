import tkinter
from tkinter import*
import random

#create root window
root=tkinter.Tk()

root.configure(bg="#5b3244")

root.title("T0 DO LIST")

root.geometry("325x275")
root.resizable(False,False)


tasks=[]



def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task():
    task=txt_input.get()
    if task!="":
        tasks.append(task)
        update_listbox()
    else:
        lbl_display["text"]="Please enter a task"
    txt_input.delete(0,"end")

def del_all():
    global tasks
    tasks=[]
    update_listbox()

def del_one():
    task=lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()

def sort_asc():
    tasks.sort()
    update_listbox()

def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()


def choose_random():
    task=random.choice(tasks)
    lbl_display["text"]=task

def show_number_of_tasks():
    number_of_tasks=len(tasks)
    msg="Number of tasks:%s"%number_of_tasks
    lbl_display["text"]=msg
    
    
def exit():
    pass

lbl_title=tkinter.Label(root,text="To-Do-List",width="18",bg="#967293")
lbl_title.grid(row=0,column=0)

lbl_display=tkinter.Label(root,text="",bg="#c2a9c0",width="18")
lbl_display.grid(row=0,column=1)

txt_input=tkinter.Entry(root,width="28",bg="#c2a9c5")
txt_input.grid(row=1,column=1)

btn_add_task=tkinter.Button(root,text="Add task",fg="#2e212d",bg="#c2a9c0",width="18",command=add_task)
btn_add_task.grid(row=1,column=0)

btn_del_all=tkinter.Button(root,text="Delete Tasks",fg="#2e212d",bg="#c2a9c0",width="18",command=del_all)
btn_del_all.grid(row=2,column=0)

btn_del_one=tkinter.Button(root,text="Delete",fg="#2e212d",bg="#c2a9c0",width="18",command=del_one)
btn_del_one.grid(row=3,column=0)

btn_sort_asc=tkinter.Button(root,text="Sort(Ascending)",fg="#2e212d",bg="#c2a9c0",width="18",command=sort_asc)
btn_sort_asc.grid(row=4,column=0)

btn_sort_desc=tkinter.Button(root,text="Sort(Descending)",fg="#2e212d",bg="#c2a9c0",width="18",command=sort_desc)
btn_sort_desc.grid(row=5,column=0)

btn_choose_random=tkinter.Button(root,text="Choose Random",fg="#2e212d",bg="#c2a9c0",width="18",command=choose_random)
btn_choose_random.grid(row=6,column=0)

btn_show_number_of_tasks=tkinter.Button(root,text="Number of tasks",fg="#2e212d",bg="#c2a9c0",width="18",command=show_number_of_tasks)
btn_show_number_of_tasks.grid(row=7,column=0)

btn_exit=tkinter.Button(root,text="Exit",fg="#2e212d",bg="#c2a9c0",width="18",command=exit)
btn_exit.grid(row=8,column=0)

lb_tasks=tkinter.Listbox(root,width="29",bg="#9e829b")
lb_tasks.grid(row=2,column=1,rowspan=7)




#starting main event
root.mainloop()