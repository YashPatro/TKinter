#08/02/25


from tkinter import *
from tkinter.ttk import *
root = Tk()
root.title('timestables!')
root.geometry('300x400')

def generate():
    n1 = num.get()
    n2 = num2.get()
    t = ''
    for i in range(n2+1):
        t += str(n1)+'x'+str(i)+'='+str(n1*i)+'\n'
    ans.configure(text = t)

Label(root,text = 'Mathematical Table').grid(row = 0,column = 1)
Label(root,text = 'Number and range').grid(row = 1,column = 0)

num = IntVar()
option = Combobox(root,textvariable = num,width = 5)
option['values'] = tuple(range(1,51))
option.grid(row  = 1, column = 1)

num2 = IntVar()
r1 = Radiobutton(root,text ='10',variable = num2,value = 10)
r1.grid(row = 1,column = 2)

r2 = Radiobutton(root,text ='20',variable = num2,value = 10)
r2.grid(row = 2,column = 2)

r3 = Radiobutton(root,text ='30',variable = num2,value = 10)
r3.grid(row = 3,column = 2)

gen = Button(root,text = 'Generate',command = generate)
gen.grid(row = 4,column = 1)

ans = Label(root)
ans.grid(row=5,column = 1) 


mainloop()