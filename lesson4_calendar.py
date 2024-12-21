#21/12/24

from tkinter import *
root = Tk()
root.geometry('300x250')
#title
root.title('Calendar')
#all labels
cal = Label(root,text = 'Calendar', font = ('Times new roman','50','bold'),bg = 'dark grey')
cal.pack()
enter = Label(root,text = 'Enter Year',font = ('Calibri','30','bold'),bg = 'light green')
enter.pack()


mainloop()