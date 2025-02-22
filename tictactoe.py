#22/02/25

from tkinter import *
from tkinter import messagebox

class tictactoe:
    def __init__(self):
        self.root = Tk()
        self.root.title('TicTacToe')
        self.cur_p = 'x'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_b()    
        self.root.mainloop()
    def create_b(self):
        for i in range(3):
            for j in range(3):
                button = Button(self.root,text = '',font = ('bold',40),width = 5,height = 3)
                button.grid(row = i,column = j)
                self.buttons[i][j] = button
    
game = tictactoe()
