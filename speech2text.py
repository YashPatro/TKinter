#22/03/25

from tkinter import *
import speech_recognition as sr
from tkinter.filedialog import *

def convert():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Start speaking')
        a = r.listen(source)
        try:
            txt = r.recognize_google(a)
        except:
            txt = 'Error: couldnt recognise voice'
        text.delete(1.0,END)
        text.insert(END,txt)


root = Tk()
root.geometry('400x300')
root.title('Speech to text')

title = Label(root,text = 'Dictate Speech into Text below!')
title.place(x = 100,y = 100)
frame = Frame(root)
frame.place(x = 50,y = 125)

text = Text(frame,width = 30,height = 4)
text.pack(pady = 30)

r = Button(frame,text = 'Record to Convert',command = convert)
r.pack(pady = 20)
root.mainloop()
