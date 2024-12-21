#21/12/24

from tkinter import *

root = Tk()
root.geometry('400x400')
'''
#label

choc = Label(root,text = 'Chocos and Ice Creams',font = ('Calibri','30','bold'),bg = 'light pink',fg = 'navy blue')
choc.pack()
#frames
frame = Frame(root)
frame.pack()

b1 = Button(frame,text = 'White',font = '25',bg = 'dark grey',fg = 'white')
b1.pack(side = LEFT)
b2 = Button(frame,text = 'Milk',font = '25',bg = 'grey',fg = 'brown')
b2.pack(side = LEFT,padx = 5)
b3 = Button(frame,text = 'Dark',font = '25',bg = 'grey',fg = '#3e2121')
b3.pack(side = LEFT)
#frame no 2
bottom_f = Frame(root)
bottom_f.pack(side = BOTTOM)

bf1 = Button(bottom_f,text = 'Tiramisu',font = '25',bg = 'light blue',fg = 'green')
bf1.pack(side = BOTTOM,pady = 25)
bf2 = Button(bottom_f,text = 'Cake',font = '25',bg = 'pink',fg = 'dark green')
bf2.pack(side = BOTTOM,pady = 25)
bf3 = Button(bottom_f,text = 'Pastry',font = '25',bg = 'beige',fg = 'dark green')
bf3.pack(side = BOTTOM,pady = 25)
'''
#list box

root.title('games')
listbox = Listbox(root,height = 10,width = 15,bg = 'light blue',fg = '#102e24',font = '40',justify = 'center')
listbox.pack()
listbox.insert(1,'Minecraft')
listbox.insert(2,'Fortnite')
listbox.insert(3,'COD')

x = Spinbox(root,from_= 0,to = 10)
x.pack()
mainloop()