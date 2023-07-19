from tkinter import*
root = Tk()
root.geometry("500x700")
root.title("Calculator")
root.configure(bg='dark grey')
def click(event):
    global sc
    text = event.widget.cget("text")
    if text == "=":
        if(sc.get().isdigit()):
            value = int(sc.get())
        else:
            value=eval(screen.get())
        sc.set(value)
        screen.update()
    elif text == "C":
        sc.set("")
        screen.update()
    else:
        sc.set(sc.get() + text)
        screen.update()

sc = StringVar()
sc.set("")
screen = Entry(root, textvariable=sc, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)
f=Frame(root, bg="DimGray")
b = Button(f, text="9", padx=28, pady=22, font="lucida 35 bold",bg="black", fg="white")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>",click)
b = Button(f, text="8", padx=28, pady=22, font="lucida 35 bold",bg="black", fg="white")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>",click)
b = Button(f, text="7", padx=28, pady=22, font="lucida 35 bold",bg="black", fg="white")
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root, bg="DimGray")
b = Button(f, text="6", padx=28, pady=22, font="lucida 35 bold",bg="black", fg="white")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>",click)
b = Button(f, text="5", padx=28, pady=22, font="lucida 35 bold",bg="black", fg="white")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>",click)
b = Button(f, text="4", padx=28, pady=22, font="lucida 35 bold",bg="black", fg="white")
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="DimGray")
b = Button(f, text="3", padx=28, pady=22, font="lucida 35 bold",bg="black", fg="white")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>",click)
b = Button(f, text="2", padx=28, pady=22, font="lucida 35 bold",bg="black", fg="white")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>",click)
b = Button(f, text="1", padx=28, pady=22, font="lucida 35 bold",bg="black", fg="white")
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>",click)
f.pack()

f2 = Frame(root,bg="DimGray", pady=10)
b1= Button(f2, text="+",padx=10, pady=8, font="lucida 20 bold",bg="purple", fg="white")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>",click)
b1= Button(f2, text="-",padx=11, pady=8, font="lucida 20 bold",bg="purple", fg="white")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>",click)
b1= Button(f2, text="*",padx=12, pady=8, font="lucida 20 bold",bg="purple", fg="white")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>",click)
b1= Button(f2, text="/",padx=11, pady=8, font="lucida 20 bold",bg="purple", fg="white")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>",click)
b1= Button(f2, text="C",padx=11, pady=8, font="lucida 20 bold",bg="purple", fg="white")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>",click)
b1= Button(f2, text="=",padx=11, pady=8, font="lucida 20 bold",bg="purple", fg="white")
b1.pack(side=LEFT, padx=9, pady=6)
b1.bind("<Button-1>",click)
f2.pack()
root.mainloop()