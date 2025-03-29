from tkinter import *
import random
from tkinter import messagebox
#window
root = Tk()
root.title("Jumbled word game")
root.geometry("400x450")
root.configure(bg="black")

#variables
score = 0
words = ['juice','monster','property','apparent','jumbled','toothpaste']
random_num = random.randrange(0,len(words),1)

#jumbler
def jumble():
    j = []
    for i in words:
        j.append(''.join(random.sample(i,len(i))))
    return j
j = jumble()
print(j)

def display():
    word_label.config(text = j[random_num])

def check():
    global score
    ans = entry.get()
    if ans == words[random_num]:
        messagebox.showinfo(message = 'Correct! You figured it out!')
        score+=1
    else:
        messagebox.showinfo(message = 'Wrong! Try again!')
    score_label.config(text = f'score: {score}')
    reset()
def reset():
    global j,random_num
    random_num = random.randrange(0,len(words),1)
    word_label.config(text = j[random_num])
    entry.delete(0,END)


#DESIGN
title_label = Label(root, text="JUMBLED WORD GAME", font=("Helvetica", 24, "bold"), fg="white", bg="black")
title_label.pack(pady=20)

word_label = Label(root, text="", font=("Helvetica", 20), fg="white", bg="black")
word_label.pack(pady=10)

entry = Entry(root, font=("Helvetica", 18))
entry.pack(pady=10, ipadx=20, ipady=5)

check_button = Button(root, text="Check", font=("Helvetica", 16), fg="light green", bg="grey", width=10, height=2, command = check)
check_button.pack(pady=10)

reset_button = Button(root, text="Reset", font=("Helvetica", 16), fg="yellow", bg="light grey", width=10, height=2,command = reset)
reset_button.pack(pady=10)

score_label = Label(root,text = f'score: {score}',font = ("Helvetica",15), fg = 'white', bg = 'black')
score_label.pack(pady = 10)
display()
root.mainloop()
