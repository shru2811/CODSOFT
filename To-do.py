from tkinter import *
from tkinter import messagebox
root = Tk()


def addTask():
    task = entry1.get()
    if task:
        listbox.insert(END, task)
        entry1.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
def delTask():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

root.geometry("500x800")
root.minsize(500,800)
root.maxsize(500,800)
root.title("TO-DO LIST:- Plan it and Execute it")
f1=Frame(root, borderwidth=3, relief=RIDGE)
f1.pack(fill=X, side=TOP)
l1 = Label(f1, text="TASKS TO-DO", bg="orange", font="comicsansms 20")
l1.pack(fill=X)
f2 = Frame(root, borderwidth=3, relief=RIDGE, bg="orange")
f2.pack(side=BOTTOM, fill=X)
b1 = Button(f2,text="Add Task", font="comicsansma 12 bold", command=addTask)
b1.pack(side=LEFT)
b2 = Button(f2,text="Delete Task", font="comicsansms 12 bold", command=delTask)
b2.pack(side=RIGHT)
task = StringVar()
entry1 = Entry(f2,textvariable="task")
entry1.pack(padx=20)
listbox = Listbox(root, width=80, height=550)
listbox.pack()
root.mainloop()