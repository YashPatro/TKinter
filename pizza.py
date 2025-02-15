#homework due 15/02/25

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Pizza App!')
root.geometry('500x400')


def order():
    n1 = num.get()
    n2 = num2.get()
    n3 = option2.get()
    t = 'You ordered '+n1+n2+n3+'(s)'
    ans.configure(text = t)

Label(root,text = 'Welcome to Pizza Hut').grid(row = 0,column = 1)
Label(root,text = 'Choose Your Pizza:').grid(row = 1,column = 0)
Label(root,text = 'Enter Quantity:').grid(row = 2,column = 0)


num = StringVar()
p = ['Vegatable Pizza','Margarita Pizza', 'BBQ Chicken Pizza']
option2 = Combobox(root,values = p,width = 5)
option2.grid(row=1,column = 1)
option = Combobox(root,textvariable = num,width = 5)
option['values'] = tuple(range(1,11))
option.grid(row  = 2, column = 1)

num2 = StringVar()
r1 = Radiobutton(root,text ='S',variable = num2, value = 'small')
r1.grid(row = 1,column = 2)

r2 = Radiobutton(root,text ='M',variable = num2,value = 'medium')
r2.grid(row = 2,column = 2)

r3 = Radiobutton(root,text ='L',variable = num2,value = 'large')
r3.grid(row = 3,column = 2)

order = Button(root,text = 'Order',command = order)
order.grid(row = 4,column = 1)

ans = Label(root)
ans.grid(row=5,column = 1) 


mainloop()



























