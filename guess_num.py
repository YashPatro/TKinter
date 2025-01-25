#25/01/25

from tkinter import *
import random
import tkinter.messagebox
root = Tk()
root.title('Guess the Number')
root.geometry('500x500')

bot = random.randint(1,20)
def ok():
    n = name_e.get()
    tkinter.messagebox.showinfo(title = 'Rules:',message = n+', you have to try and guess the number that the bot has chosen between 1 and 20 to win. Good luck '+n+'!')

def guess():
    global bot
    user = int(guess_e.get()) 
    if user<bot:
        tkinter.messagebox.showinfo(message = 'Wrong! Your guess was too low!')
    elif user>bot:
        tkinter.messagebox.showinfo(message = 'Wrong! Your guess was too high!')
    else:
        tkinter.messagebox.showinfo(message = 'Well done you got it right! I bet it wasnt first try!')
Label(root,text = 'Welcome to our Game!', font = 30).place(x=190,y = 5)
Label(root,text = 'Whats your name?',font = 20).place(x = 10,y = 60)
name_e = Entry(root,width = 17,font = 17)
name_e.place(x = 10,y = 90)

ok_b = Button(root,text = 'OK!',font = 20,command = ok)
ok_b.place(x  = 300,y = 68)


Label(root,text = 'Take a Guess',font = 20).place(x = 10,y = 200)
guess_e = Entry(root,width = 17,font = 17)
guess_e.place(x = 10,y = 230)

guess_b = Button(root,text = 'Guess',font = 20, command = guess)
guess_b.place(x  = 300,y = 218)



mainloop()