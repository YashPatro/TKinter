#22/02/25

from tkinter import *
from tkinter import messagebox

class tictactoe:
    def __init__(self,root):
        self.root = root
        self.root.title('TicTacToe')
        self.cur_p = 'x'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_b()    
    def create_b(self):
        for i in range(3):
            for j in range(3):
                button = Button(self.root,text = '',font = ('bold',40),width = 5,height = 3)
                button.grid(row = i,column = j)
                self.buttons[i][j] = button
    def check_win(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != '':
                return True
        
        for j in range(3):
            if self.buttons[0][j]['text'] == self.buttons[1][j]['text'] == self.buttons[2][j]['text'] != '':
                return True
            
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '':
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '':
            return True
        return False

    def pl_click(self,r,c):
        if self.buttons[r][c]['text'] == '' and not self.check_win():
            self.buttons[r][c]['text'] == self.cur_p
            if check_win():
                messagebox.showinfo(message = f'The Game is over, player {self.cur_p} won!!!')
            elif self.board_full():
                messagebox.showinfo(message = f'The Game is a Tie!!!')
            else:
                if cur_p == 'x':
                    cur_p = 'o'
                else:
                    cur_p = 'x'
                    


    def board_full(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j]['text'] == '':
                    return False
        return True






root = Tk()
game = tictactoe(root)
mainloop()