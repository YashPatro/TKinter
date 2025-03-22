from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *

root = Tk()
root.title("Student Grading System")

students = {}

def open_file():
    global students
    listbox.delete(0, END)
    students.clear()
    file = askopenfile(title='Open file')
    if file:
        students = eval(file.read())
        for name in students.keys():
            listbox.insert(END, name)
        messagebox.showinfo("Success", "Student records loaded successfully.")
    else:
        messagebox.showerror("Error", "No file selected.")

def save_file():
    file = asksaveasfile(defaultextension='.txt')
    if file:
        print(students, file=file)
        messagebox.showinfo("Success", "Student records saved successfully.")
    else:
        messagebox.showerror("Error", "Save cancelled.")

frame = Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label_title = Label(frame, text="Student Grading System")
label_title.grid(row=0, column=0, columnspan=2, pady=5)

button_open = Button(frame, text="Open", width=10, command=open_file)
button_open.grid(row=0, column=2, padx=5)

listbox = Listbox(frame, width=40, height=8)
listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

label_name = Label(frame, text="Name:")
label_name.grid(row=2, column=0, pady=2)
entry_name = Entry(frame, width=25)
entry_name.grid(row=2, column=1, columnspan=2, pady=2)

label_subject = Label(frame, text="Subject:")
label_subject.grid(row=3, column=0, pady=2)
entry_subject = Entry(frame, width=25)
entry_subject.grid(row=3, column=1, columnspan=2, pady=2)

label_grade = Label(frame, text="Grade:")
label_grade.grid(row=4, column=0, pady=2)
entry_grade = Entry(frame, width=25)
entry_grade.grid(row=4, column=1, columnspan=2, pady=2)

label_email = Label(frame, text="Email:")
label_email.grid(row=5, column=0, pady=2)
entry_email = Entry(frame, width=25)
entry_email.grid(row=5, column=1, columnspan=2, pady=2)

label_comments = Label(frame, text="Comments:")
label_comments.grid(row=6, column=0, pady=2)
entry_comments = Entry(frame, width=25)
entry_comments.grid(row=6, column=1, columnspan=2, pady=2)

button_save = Button(frame, text="Save", width=30, command=save_file)
button_save.grid(row=7, column=0, columnspan=3, pady=10)

root.mainloop()
