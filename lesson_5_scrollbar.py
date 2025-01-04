from tkinter import *
root = Tk()
root.geometry('400x400')

#label
l1 = Label(root,text = 'Items',font = ('Calibri','20','bold'),bg = 'light blue')
l1.pack()

#scrollbar
s1 = Scrollbar(root)
s1.pack(side = RIGHT,fill = Y)

l2 = Listbox(root,yscrollcommand = s1.set)
for i in range(1,100):
    l2.insert(END,'list'+str(i))
l2.pack(side = LEFT,fill = BOTH)

s1.config(command = l2.yview)


mainloop()