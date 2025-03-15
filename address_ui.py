#08/03/25 

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *  
root = Tk()
root.title("My Address Book")

book = {}
def delete():
    select = listbox.curselection()
    if select:
        del book[listbox.get(select)]
        listbox.delete(select)
        clear_all()
    else:
        messagebox.showerror(message = 'please click an address name')
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
def open():
    global book
    listbox.delete(0,END)
    book.clear()    
    file = askopenfile(title = 'open file')
    if file:
        book = eval(file.read())
        for i in book.keys():
            listbox.insert(END,i)
    else:
        messagebox.showerror("Error", "Please select a name from the list.")
def save():
    file = asksaveasfile(defaultextension = '.txt')
    if file:
        print(book,file = file)
        listbox.delete(0,END)
        book.clear()
        messagebox.showinfo("Success", "Contacts saved successfully.")
    else:
        messagebox.showerror(message = "The address book has not been saved")
def pop_up(event):
    window = Toplevel(root)
    select = listbox.curselection()
    info = ''
    if select:
        key = listbox.get(select)
        details = book[key]
        info = 'name:' + key + '\n'
        info += 'address:' + details[0] +'\n'
        info += 'mobile:' + details[1] + '\n'
        info += 'email:' + details[2] +'\n'
        info += 'bday:' + details[3] + '\n'
    label = Label(window,text = info)
    label.pack()

frame = Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label_title = Label(frame, text="My Address Book")
label_title.grid(row=0, column=0, columnspan=2, pady=5)

button_open = Button(frame, text="Open", width=10,command = open)
button_open.grid(row=0, column=2, padx=5)


listbox = Listbox(frame, width=40, height=8)
listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
listbox.bind('<<ListboxSelect>>',pop_up)

button_edit = Button(frame, text="Edit", width=10, command = edit)
button_edit.grid(row=2, column=0, pady=5, padx=5)

button_delete = Button(frame, text="Delete", width=10,command = delete)
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

button_save = Button(frame, text="Save", width=30, command = save)
button_save.grid(row=9, column=0, columnspan=3, pady=5)



mainloop()
