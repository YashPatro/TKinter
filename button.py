#14/12/24
from tkinter import *
#making window the parent
root = Tk()
#making minimun size or/and initial position of window - first number is size, second two number are x,y
root.geometry('200x200+100+200')
root.config(background = 'sky blue')
#making a button
b1 = Button(root,text = 'This is a button',bd = '10', background = 'light green')
#geometry method no.1: pack decides where the button will be
b1.pack(side = 'left')


mainloop()





