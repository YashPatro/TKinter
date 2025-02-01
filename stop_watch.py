#01/02/12

from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.title('Timer')
root.geometry('500x500')
 
hr = StringVar()
m = StringVar()
sec = StringVar()
hr.set('00')
m.set('00')
sec.set('00')

def timer():
    
    tot = int(hr.get())*3600+int(m.get())*60+int(sec.get())
    while tot>-1:
        mins,secs = divmod(tot,60)
        hrs = 0
        if mins > 60:
            hrs,mins = divmod(mins,60) 
        hr.set(hrs)
        m.set(mins)
        sec.set(secs)
        root.update()
        time.sleep(1)
        if tot == 0:
            messagebox.showinfo(message = 'Times up!!!')
        tot-=1
            
hr_e = Entry(root,width = 2,font = 30,textvariable = hr)
hr_e.place(x = 200,y = 100)

min_e = Entry(root,width = 2,font = 30,textvariable = m)
min_e.place(x = 240,y = 100)

sec_e = Entry(root,width = 2,font = 30,textvariable = sec)
sec_e.place(x = 280,y = 100)


set_t = Button(root,text = 'Set the timer countdown!',font = ('Calibri',10,'bold'),command = timer)
set_t.place(x = 175,y = 200)
mainloop()