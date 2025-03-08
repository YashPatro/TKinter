from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("My Address Book")

book = {}
def clear_all():
    entry_name.delete(0,END)
    entry_address.delete(0,END)
    entry_mobile.delete(0,END)
    entry_email.delete(0,END)
    entry_birthday.delete(0,END)
def add():
    name = entry_name.get()
    address = entry_address.get()
    mobile = entry_mobile.get()
    email = entry_email.get()
    bday = entry_birthday.get()
    if name == '':
        message.showinfo(message = 'Please enter the name before pressing the add button.')
    else:
        if name not in book:
            listbox.insert(END,name)
        book[name] = (address,mobile,email,bday)        
        clear_all()
    print(book)

def edit():
    select = listbox.curselection()
    
    if select:
        entry_name.insert(0,listbox.get(select))
        values = book[entry_name.get()]
        entry_address.insert(0,values[0])
        entry_mobile.insert(0,values[1])
        entry_email.insert(0,values[2])
        entry_birthday.insert(0,values[3])
    else:
        messagebox.showinfo(message = 'Please select a name before clicking this button')
frame = Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label_title = Label(frame, text="My Address Book")
label_title.grid(row=0, column=0, columnspan=2, pady=5)

button_open = Button(frame, text="Open", width=10)
button_open.grid(row=0, column=2, padx=5)


listbox = Listbox(frame, width=40, height=8)
listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)


button_edit = Button(frame, text="Edit", width=10, command = edit)
button_edit.grid(row=2, column=0, pady=5, padx=5)

button_delete = Button(frame, text="Delete", width=10)
button_delete.grid(row=2, column=1, pady=5, padx=5)


label_name = Label(frame, text="Name:")
label_name.grid(row=3, column=0, pady=2)


entry_name = Entry(frame, width=25)
entry_name.grid(row=3, column=1, columnspan=2, pady=2)

label_address = Label(frame, text="Address:")
label_address.grid(row=4, column=0, pady=2)

entry_address = Entry(frame, width=25)
entry_address.grid(row=4, column=1, columnspan=2, pady=2)

label_mobile = Label(frame, text="Mobile:")
label_mobile.grid(row=5, column=0, pady=2)

entry_mobile = Entry(frame, width=25)
entry_mobile.grid(row=5, column=1, columnspan=2, pady=2)

label_email = Label(frame, text="Email:")
label_email.grid(row=6, column=0, pady=2)

entry_email = Entry(frame, width=25)
entry_email.grid(row=6, column=1, columnspan=2, pady=2)

label_birthday = Label(frame, text="Birthday:")
label_birthday.grid(row=7, column=0, pady=2)

entry_birthday = Entry(frame, width=25)
entry_birthday.grid(row=7, column=1, columnspan=2, pady=2)


button_update_add = Button(frame, text="Update/Add", width=10,command = add)
button_update_add.grid(row=8, column=2, pady=5)

button_save = Button(frame, text="Save", width=30)
button_save.grid(row=9, column=0, columnspan=3, pady=5)



mainloop()
