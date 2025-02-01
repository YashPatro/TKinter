#25/01/25
'''from tkinter import *
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
'''# color digital clock hw
from tkinter import *
import time
import random

root = Tk()
root.title('Clock in GMT')

def clock():
    t1 = time.strftime('%H:%M:%S %p')
    

    rf = random.randint(0, 255)
    gf = random.randint(0, 255)
    bf = random.randint(0, 255)

    rb = random.randint(0, 255)
    gb = random.randint(0, 255)
    bb = random.randint(0, 255)

    fg_colour = f"#{rf:02x}{gf:02x}{bf:02x}"
    bg_colour = f"#{rb:02x}{gb:02x}{bb:02x}" 
    
    t2.config(text=t1,fg=fg_colour,bg=bg_colour)
    
    t2.after(1000, clock)

label = Label(root, text="My Digital Clock", font=('Arial', 20, 'bold'), fg='black', bg='lightgrey')
label.pack(pady=10)

t2 = Label(root, font=('times new roman', 40, 'bold'), padx=10, pady=10)
t2.pack(pady=20)

clock()

mainloop()
