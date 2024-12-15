#15/12/24
from tkinter import *
from tkinter.ttk import *
root = Tk()
root.title('Menu')

m1 = Menu(root)

#file menu
file = Menu(m1,tearoff = 0)

m1.add_cascade(label = 'file',menu = file)
file.add_command(label = 'New Text File',command = None)
file.add_command(label = 'New File', command = None)
file.add_command(label = 'New Window', command = None)
file.add_separator()
file.add_command(label = 'Open File', command = None)
file.add_command(label = 'Exit', command = root.destroy)

#edit menu
edit = Menu(m1,tearoff = 0)

m1.add_cascade(label = 'Edit',menu = edit)
edit.add_command(label = 'Undo',command = None)
edit.add_command(label = 'Redo', command = None)
edit.add_separator()
edit.add_command(label = 'Cut', command = None)
edit.add_command(label = 'Copy', command = None)
edit.add_command(label = 'Paste', command = None)








root.config(menu = m1)
mainloop()