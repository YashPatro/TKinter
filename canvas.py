from tkinter import *
from tkinter.colorchooser import askcolor


class Paint:
    def __init__(self):
        self.root = Tk()
        #buttons
        self.pen_button = Button(self.root, text = 'pen',command = self.use_pen)
        self.pen_button.grid(row=0, column= 0)

        self.clr_button = Button(self.root, text = 'clr', command = self.color)
        self.clr_button.grid(row=0, column= 1)

        self.erase_button = Button(self.root, text = 'eraser', command = self.erase)
        self.erase_button.grid(row=0, column= 2)

        self.clearC_button = Button(self.root, text = 'clear canvas',command = self.clear)
        self.clearC_button.grid(row=0, column= 3)

        #scale
        self.scale = Scale(self.root, from_=1, to=10,orient= HORIZONTAL)
        self.scale.grid(row=0, column= 4)

        self.canvas = Canvas(self.root,bg = 'white',width = 500,height= 500)
        self.canvas.grid(row=1,columnspan=5)
        self.setup()
        mainloop()
    def setup(self):
        self.x = None
        self.y = None
        self.width = self.scale.get()
        self.clr = 'black'
        self.cur = self.pen_button
        self.canvas.bind('<B1-Motion>',self.draw)
        self.canvas.bind('<ButtonRelease-1>',self.reset)
    def activate(self,button):
        self.cur.config(relief = RAISED)
        button.config(relief = SUNKEN)
        self.cur = button
    def use_pen(self):
        self.activate(self.pen_button)
        if self.clr == 'white':
            self.clr = 'black'
        else:
            self.clr = self.clr
    def erase(self):
        self.activate(self.erase_button)
        self.clr= 'white'

    def color(self):
        self.clr = askcolor(color=self.clr)[1]
    def clear(self):
        self.canvas.delete('all')
    def draw(self,event):
        self.width = self.scale.get()
        if self.x and self.y:
            self.canvas.create_line(self.x,self.y,event.x,event.y,width = self.width,fill = self.clr)
        self.x = event.x
        self.y = event.y
    def reset(self,event):
        self.x,self.y = None,None

painter = Paint()