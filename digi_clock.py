#25/01/25
from tkinter import *
import time

root = Tk()
root.title('Clock in GMT')

def clock():
    t1 = time.strftime('%H:%M:%S %p')
    t2.config(text = t1)
    t2.after(1000,clock)

t2 = Label(root,font = ('times new roman',30,'bold'),fg = 'dark blue',bg = 'orange')
t2.pack()
clock()



mainloop()