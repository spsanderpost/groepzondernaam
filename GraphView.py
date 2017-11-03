# @author Yoran Ypey

from tkinter import *
from random import randint
import time
from threading import Thread


class GraphView:

    def __init__(self,sunblind,model):
        #initiate variables
        self.model = model
        self.sunblind = sunblind
        self.root = Tk()
        self.root.title("Live Data with ID.NO %s" % (self.sunblind.id))
        self.canvas = Canvas(self.root, width=810, height=600 ,relief=SUNKEN, bd=1)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.yvalue = 0
        self.s = 1
        self.x2 = 50
        self.y2 = 550 - 5 * (self.yvalue / 2)
        self.create_window()

        #self.t1 = Thread(target=self.update, daemon=True)
       # self.t1.start()

  #  def update(self):
  #      try:
  #         self.root.after(1000,self.step)
  #         self.root.mainloop()
  #      except:
  #          pass
    def step(self):
        self.yvalue = (randint(0,100) /2)
        if self.s == 16:
            # new frame
            self.s = 1
            self.x2 = 50
            self.canvas.delete('temp')
        x1 = self.x2
        y1 = self.y2
        self.x2 = 50 + self.s*50
        self.y2 = 550 - 5 * self.yvalue
        self.canvas.create_line(x1, y1, self.x2, self.y2, fill='orange', tags='temp')
        self.s = self.s+1
        self.canvas.after(1000, self.step)

    def create_window(self):
        #Y-labels
        templabel = Label(self.canvas,text='Temp.',fg='Orange')
        templabel.pack()
        self.canvas.create_window(18,315,window=templabel)

        celciuslabel = Label(self.canvas,text='In °C',fg='Orange')
        celciuslabel.pack()
        self.canvas.create_window(18,333,window=celciuslabel)

        #X-labels
        xlabel = Label(self.canvas,text='Tijd in seconden',fg='Orange')
        xlabel.pack()
        self.canvas.create_window(400,575,window=xlabel)

        self.canvas.create_line(50,550,800,550, width=2) # x-axis
        self.canvas.create_line(50,550,50,50, width=2)    # y-axis

        # x-axis
        for i in range(16):
            x = 50 + (i * 50)
            self.canvas.create_line(x,550,x,50, width=1, dash=(2,5))
            self.canvas.create_text(x,550, text='%d'% (i), anchor=N)

        # y-axis
        for i in range(11):
            y = 550 - (i * 50)
            self.canvas.create_line(50,y,800,y, width=1, dash=(2,5))
            self.canvas.create_text(40,y, text='%d'% (i*10/2), anchor=E)

        #create buttons
        Button(self.root,text='Read out Data', command=lambda:self.start()).pack()
        Button(self.root, text='Close Window', command=lambda: self.close()).pack()

    def close(self):
        self.root.destroy()

    def start(self):
        self.step()

