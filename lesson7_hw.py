from tkinter import *


def calculate_distance():
    time = float(time_entry.get())
    speed = float(speed_entry.get())
    distance = time * speed
    result_label.config(text=f"Distance: {distance} km")
    
root = Tk()
root.title("Distance Calculator")

#tiem
time_l = Label(root, text="Time (hours):")
time_l.grid(row=0, column=0, padx=10, pady=10)

time_entry = Entry(root)
time_entry.grid(row=0, column=1, padx=10, pady=10)

#speed
speed_label = Label(root, text="Speed (km/h):")
speed_label.grid(row=1, column=0, padx=10, pady=10)

speed_entry = Entry(root)
speed_entry.grid(row=1, column=1, padx=10, pady=10)

#func
calculate_button = Button(root, text="Calculate Distance", command=lambda: calculate_distance())
calculate_button.grid(row=2, column=1, pady=20)


result_label = Label(root, text="Distance: ")
result_label.grid(row=3, column=1, pady=10)


root.mainloop()
