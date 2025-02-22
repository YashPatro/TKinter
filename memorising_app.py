#15/-2/25
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

def save():
    filetypes = [('Text Document', '*.txt')]
    f = asksaveasfile(filetypes=filetypes, defaultextension='.txt') 
    if f is not None:
        for i in text_box.get(0,END):
            print(i,file = f)
        text_box.delete(0, END)

def open_f():
    file = askopenfile(mode='r', filetypes=[('All Files', '*.*')])
    if file is not None:
        content = file.readlines()
        text_box.delete(0, END) 
        for i in content:
            text_box.insert(END, i)

def add():
    text_box.insert(END,change.get())
    change.delete(0,END)
root = Tk()
root.geometry('600x700')
save_b = Button(root, text='Save',command = save )
save_b.pack()

def delete():
    cur = text_box.curselection()
    if cur:
        text_box.delete(cur)
    else:
        messagebox.showinfo(message = 'Make a Selection First!')

#entry button
change = Entry(root, width=20)
change.pack()

#add
add_b = Button(root, text='Add',command = add)
add_b.pack()
frame = Frame(root)
frame.pack()
#text wudget
text_box = Listbox(frame, width=70, height=40, bg='light blue')
text_box.grid(row = 0,column = 1)

#open button
open_b = Button(frame, text='Open', command=open_f)
open_b.grid(row = 0,column = 0)

delete = Button(frame,text = 'Delete',command = delete)
delete.grid(row = 0,column = 2)











mainloop()
