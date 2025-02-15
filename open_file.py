#1502/25

from tkinter import *

from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
root = Tk()
root.title('Open A File')

def open_f():
    file = askopenfile(mode = 'r',filetypes = [('All Files','*.*')])
    if file is not None:
        c = file.read()
        print(c)
    
def save():
    t = [('Text Document','*.txt')]
    f = asksaveasfile(filetypes = t, defaultextension = t)
    if f is not None:
        text = txt.get()
        print(text,file = f)
        txt.delete(0,END)
open_b = Button(root,text = 'Open',command =  open_f).pack()
save = Button(root,text = 'Save',command = save).pack()

txt = Entry(root,width = 20)
txt.pack()


mainloop()












