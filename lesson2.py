#15/12/24
from tkinter import *

root = Tk()
root.title('Title')
root.geometry('671x485')
root.config(background = 'light pink')

#username
u1 = Label(root,text = 'Username: ', font = ('Calibri',15,'bold'),bg = 'light blue', fg = 'black')
u1.place(x = 100, y = 100)

#password
p1 = Label(root,text = 'Password: ', font = ('Calibri',15,'bold'),bg = 'light blue', fg = 'black')
p1.place(x = 100, y = 200)

#entry
e1 = Entry(root,width = 30, font = ('Ariel', 15, 'normal'),fg = 'dark grey')
e1.place(x = 210, y = 100)

e2 = Entry(root,show = '*',width = 30, font = ('Ariel', 15, 'normal'),fg = 'dark grey')
e2.place(x = 210, y = 200)

#submit button
s1 = Button(root,text = 'Submit',font = ('Time New Roman',15,'bold'))
s1.place(x = 300, y = 300)

mainloop()