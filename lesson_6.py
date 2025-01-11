#11/01/25
from tkinter import *

# main window
root = Tk()
root.title("F° to C°")
root.config(bg = 'light blue')

def celsius():
    cel = (float(entry_txt.get()) - 32) * 5/9
    c_txt.delete('1.0',END)
    c_txt.insert(END,cel)

entry = Label(root,text = 'Enter a tempurature in Fahrenheit:',bg = 'dark blue',fg  = 'red')
entry.grid(row  = 0, column =0,pady = 5)
entry_txt = Entry(root,width = 12)
entry_txt.grid(row = 0, column =3,pady = 5 )

c = Label(root,text = 'Celsius',bg = 'red',fg  = 'dark blue')
c.grid(row = 1,column = 0,pady = 10)
c_txt = Text(root,height = 1,width = 10)
c_txt.grid(row = 1,column = 3,pady = 10)

button = Button(root,text = 'Change',command = celsius)
button.grid(row = 2, column = 3)

mainloop()