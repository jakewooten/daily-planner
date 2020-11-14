from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from datetime import *


m1 = PanedWindow(height=550, width=1000)
m1.pack(fill=BOTH, expand=1)

# left = Label(m1, text="left pane")
# m1.add(left)
lb = Listbox(m1, selectmode=SINGLE)
lb.insert(1, "Python")
lb.insert(2, "Perl")
lb.insert(3, "C")
lb.insert(4, "PHP")
lb.insert(5, "JSP")
lb.insert(6, "Ruby")

m1.add(lb)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Label(m2, text="top pane")
m2.add(top)

def remove_list():
   lb.delete(lb.curselection())
def add_list():
   if e.get() != "":
      lb.insert(END, e.get())
      e.delete(0, END)
   add_button.config(bg="pink")
def submit_list():
   d = date.today().strftime("%m/%d/%y")
   if d == cal.get_date():
      todo_list = lb.get(0,END)
      print(todo_list)
   elif d != cal.get_date():
      messagebox.showinfo("Error", "Cannot submit list from a non-current date.")

e = Entry(m2)
m2.add(e)

add_button = Button(m2, text="Add to List", command=add_list)
m2.add(add_button)

remove_button = Button(m2, text="Delete From List", command=remove_list)
m2.add(remove_button)

submit_button = Button(m2, text="Submit List", command=submit_list)
m2.add(submit_button)

cal = Calendar(m2,selectmode="day", foreground="black", selectforeground="red")
bottom = Label(m2, text="bottom pane")
m2.add(bottom)
m2.add(cal)




mainloop()