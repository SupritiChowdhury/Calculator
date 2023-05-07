from tkinter import*
def click(event):
    global scvalue
    Text=event.widget.cget("text")
    print(Text)
    if Text=="=":
        if scvalue.get().isdigit():
            Value = int(scvalue.get())
        else:
            value = eval(scvalue.get())
            scvalue.set(value)
            screen.update()
    elif Text=="C":
       scvalue.set("")
       screen.update()
    else:
        scvalue.set(scvalue.get()+Text)
        screen.update()

root = Tk()

root.geometry("650x750")
root.title("Calculator")
root.wm_iconbitmap(r'Icon')
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue,font="popin 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)


f = Frame(root, bg="grey")
b = Button(f, text="7", padx=18, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=20, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)

b = Button(f, text="9", padx=20, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=20, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=18, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)


f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="4", padx=20.5, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=20, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=20, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=20, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=20, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)


f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="1", padx=12, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=20, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=20, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=20, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)


b = Button(f, text="+", padx=12, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)


f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="0", padx=25, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=20, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=20, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)

b = Button(f, text="(", padx=20, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)

b = Button(f, text=")", padx=25, pady=18, font="popin 35 bold")
b.pack(side=LEFT, padx=15, pady=20)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()
