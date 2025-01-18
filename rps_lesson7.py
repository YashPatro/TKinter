from tkinter import *
import random
# main window
root = Tk()
root.title("Rock Paper")
root.geometry('500x500')
c_score = 0
pl_score = 0
options = ['rock','paper','scissors']


def pl_win():
    global pl_score,c_score
    pl_score+=1
    start.config(text = 'You have won!!!',fg = 'green')
    score_pl.config(text="Your Score:"+str(pl_score))
    score_c.config(text = 'Bot Score:'+str(c_score))
def c_win():
    global pl_score,c_score
    c_score+=1
    start.config(text = 'The Bot has won!!!',fg = 'red')
    score_pl.config(text="Your Score:"+str(pl_score))
    score_c.config(text = 'Bot Score:'+str(c_score))

def tie():
    global pl_score,c_score
    start.config(text = 'It appears to be a tie!',fg = 'purple')
    score_pl.config(text="Your Score:"+str(pl_score))
    score_c.config(text = 'Bot Score:'+str(c_score))


def rps(pl):
    global pl_score,c_score
    bot = random.choice(options)
    sel_pl.config(text = 'You selected:'+pl)
    sel_c.config(text = "Bot selected:"+bot)

    if pl==bot:
        tie()

    elif pl == options[0] and bot == options[1]:
        c_win()
    elif pl == options[0] and bot == options[2]:
        pl_win()
    elif pl == options[1] and bot == options[0]:
        pl_win()
    elif pl == options[1] and bot == options[2]:
        c_win()
    elif pl == options[2] and bot == options[1]:
        pl_win()
    elif pl == options[2] and bot == options[0]:
        c_win()

Label(root, text="Rock Paper Scissors",font = ('Calibri',30),fg = 'grey').pack()
start = Label(root, text="Lets start the game",font = ('Calibri',15),fg = 'green')
start.pack(pady = 3)
f1 = Frame(root)
f1.pack()
Label(f1, text="Options:",font = ('Calibri',15),fg = 'grey').grid(row = 0,column =0)

rock = Button(f1,text = 'Rock',bg = 'pink', command = lambda:rps(options[0]))
rock.grid(row = 0,column = 2,pady = 3)


paper = Button(f1,text = 'Paper',bg = 'grey', command = lambda:rps(options[1]))
paper.grid(row = 0,column = 3,pady = 3)

scissors = Button(f1,text = 'Scissors',bg = 'light blue', command = lambda:rps(options[2]))
scissors.grid(row = 0,column = 4,pady = 3)

f2 = Frame(root)
f2.pack()

Label(f2, text="Score:",font = ('Calibri',15),fg = 'grey').grid(row =  1,column =0,padx = 2)


score_pl =Label(f2, text="Your Score:",font = ('Calibri',15),fg = 'grey')
score_pl.grid(row =  1,column =1,padx = 2)
score_c = Label(f2, text="Bot Score:",font = ('Calibri',15),fg = 'grey')
score_c.grid(row =  1,column =2,padx =2)
sel_pl = Label(f2, text="You selected:",font = ('Calibri',15),fg = 'grey')
sel_pl.grid(row = 2,column =1,padx = 3)
sel_c = Label(f2, text="Bot selected:",font = ('Calibri',15),fg = 'grey')
sel_c.grid(row =  2,column =2,padx = 2)


mainloop()