from tkinter import *

# main window
root = Tk()
root.title("Weight Converter")

def convert():
    g = float(entry_kg.get())*1000 
    lb = float(entry_kg.get())*2.20462 
    oz = float(entry_kg.get())*35.274
    g_txt.delete('1.0',END)
    g_txt.insert(END,g)
    p_txt.delete('1.0',END)
    p_txt.insert(END,lb)
    o_txt.delete('1.0',END)
    o_txt.insert(END,oz)

    

# widgets
Label(root, text="Enter the weight in Kg:").grid(row=0, column=0, padx=10, pady=5)
entry_kg = Entry(root)
entry_kg.grid(row=0, column=1, pady=5)

button_convert = Button(root, text="Convert",command = convert)
button_convert.grid(row=0, column=2, pady=5)

Label(root, text="Gram").grid(row=1, column=0, padx=10, pady=5)
g_txt = Text(root,height = 1, width = 15)
g_txt.grid(row= 2, column = 0,pady = 2 )

Label(root, text="Pounds").grid(row=1, column=1, pady=5)
p_txt = Text(root,height = 1, width = 15)
p_txt.grid(row= 2, column = 1,pady = 2 )

Label(root, text="Ounce").grid(row=1, column=2, pady=5)
o_txt = Text(root,height = 1, width = 15)
o_txt.grid(row= 2, column = 2,pady = 2 )



root.mainloop()
