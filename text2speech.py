from tkinter import *
from gtts import gTTS
import os

def convert():
    txt = gTTS(text=entry.get(),lang = 'de',slow=False)
    txt.save('Speech.wav')
    os.system('Speech.wav')


root = Tk()
root.title('Text to speech')
root.geometry('400x350')
frame1 = Frame(root,bg = 'sky blue',height = '100')
frame1.pack(fill = X)

title = Label(frame1,text = 'Text to Speech!!!',font = ('Arial',20,'bold'))
title.place(x = 85,y=50)

frame2 = Frame(root,height = '300',bg = 'light green')
frame2.pack(fill = X)

entry = Entry(frame2,width = '50')
entry.pack(pady = 50)

play_b = Button(frame2, text = 'Play/Convert',command = convert)
play_b.pack(pady = 50)


root.mainloop()

