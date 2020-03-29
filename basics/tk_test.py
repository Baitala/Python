from tkinter import *

def handler1(event):
    print("Hello World!", event.x, event.y)

def handler2(event):
    exit()

root = Tk()
hello_label = Label(root, text="Hello world", font="Times 40")
hello_label.pack()

hello_label.bind('<Button-1>', handler1)
hello_label.bind('<Button-3>', handler2)

root.mainloop()

