from tkinter import *
from tkinter import messagebox

# Create the main application window
root = Tk()
root.title("Order Form")
root.geometry("500x600")
root.configure(bg="red")

# Email field
email_label = Label(root, text="Email", bg="red", fg="black")
email_label.pack(pady=5)
email_entry = Entry(root, width=50)
email_entry.pack()

# Password field
password_label = Label(root, text="Password", bg="red", fg="black")
password_label.pack(pady=5)
password_entry = Entry(root, show="*", width=50)
password_entry.pack()

# Food selection field
food_label = Label(root, text="What food would you like: Chicken sandwich, B.L.T, Veg sandwich? or None", bg="red", fg="black")
food_label.pack(pady=5)
food_entry = Entry(root, width=50)
food_entry.pack()
food_quantity_spinbox = Spinbox(root, from_=1, to=100, width=5)
food_quantity_spinbox.pack()

# Beverage selection field
beverage_label = Label(root, text="What beverage would you like: Cola, Fanta, Orange Juice, Water or None?", bg="red", fg="black")
beverage_label.pack(pady=5)
beverage_entry = Entry(root, width=50)
beverage_entry.pack()
beverage_quantity_spinbox = Spinbox(root, from_=1, to=100, width=5)
beverage_quantity_spinbox.pack()

#Dessert
dessert_label = Label(root, text="What dessert would you like: An Ice Cream, an Ice Lolly or a Chocolate Cake or None?", bg="red", fg="black")
dessert_label.pack(pady=5)
dessert_entry = Entry(root, width=50)
dessert_entry.pack()
dessert_quantity_spinbox = Spinbox(root, from_=1, to=100, width=5)
dessert_quantity_spinbox.pack()

#Submit button
submit_button = Button(root, text="Submit Order", width=20, bg="gray", fg="black")
submit_button.pack(pady = 20)

#Box under the submit button
output_box = Entry(root, width=50, bg="white", fg="black")
output_box.pack(pady = (0, 20))

root.mainloop()
