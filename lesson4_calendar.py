#21/12/24

from tkinter import *
import calendar
root = Tk()
root.geometry('300x250')
#title
root.title('Calendar')

#calndar
def cal():
    win = Tk()
    win.config(background = 'light pink')
    win.title('Calendar')
    win.geometry('400x400')
    year = int(entry.get())
    cal2 = calendar.calendar(year)
    #text widget
    txt = Text(win,font =('Consolas 10'),wrap = 'none',height = 60,width = 80)
    txt.insert('1.0',cal2)
    txt.grid()

    win.mainloop()
#all labels
cal = Label(root,text = 'Calendar', font = ('Times new roman','50','bold'),bg = 'dark grey')
cal.pack()
enter = Label(root,text = 'Enter Year',font = ('Calibri','20','bold'),bg = 'light green')
enter.pack()

entry = Entry(root,font = ('Calibri','15','bold'))
show_c = Button(root,text = 'Show Calendar',bg = 'red',command = cal)
exit_b = Button(root,text = 'Exit',bg = 'red',command = exit)
entry.pack()
show_c.pack()
exit_b.pack()

#calendar

mainloop()