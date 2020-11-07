from tkinter import *

from tkinter import messagebox

root = Tk()
root.geometry("900x600")
def helloCallBack():
   msg = messagebox.showinfo( "Hello Python", "Hello World")

B = Button(root, text = "Hello", command = helloCallBack)
B.place(x=450, y=300)
root.mainloop()
