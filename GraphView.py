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
        #Root,Canvas and Frame
        self.root = Tk()
        self.root.title("Live Data ID.NO %s" % (self.sunblind.id))
        self.frame = Frame(self.root,width=1200,height=700,bd=1)
        self.frame.pack()
        self.seconds = 0
        self.minutes = 0
        #values for temp_graph
        self.tempvalue = 0
        self.s = 1
        self.x2 = 50
        self.y2 = 550 - 5 * (self.tempvalue / 2)
        #values for the distance_graph
        self.distancevalue = 0
        self.ds = 1
        self.xx2 = 50
        self.yy2 = 550 - 5 * (self.distancevalue / 2)
        #booleans that are used to show the views
        self.livedata = False
        self.temp_graph = False
        self.distance_graph = False

        #graph buttons
        self.show_temp = Button(self.root, text="Show temperature graph", command=lambda: self.temp_graph_window()).pack(side=LEFT)  # create
        self.show_distance = Button(self.root, text="Show distance graph", command=lambda: self.distance_window()).pack(side=LEFT)
        #live_data button
        self.show_livedata = Button(self.root,text="Show live data",command=lambda:self.live_data_window()).pack(side=LEFT)
        #self.delete_livedata = Button(self.root, text="Delete live data", command=lambda: self.destroy_canvas(self.live_data_window())).pack(side=RIGHT)
        #close button
        self.close_button = Button(self.root, text='Close Window', command=lambda: self.close()).pack(side=LEFT)

        self.step()


    def step(self):
        #Execute once every second, updates the graph and the infoframe
        if self.temp_graph:
            self.tempvalue = (randint(0,100) /2)
            if self.s == 16:
                # new frame
                self.s = 1
                self.x2 = 50
                self.canvas.delete('temp')
            x1 = self.x2
            y1 = self.y2
            self.x2 = 50 + self.s*50
            self.y2 = 550 - 5 * self.tempvalue
            self.canvas.create_line(x1, y1, self.x2, self.y2, fill='orange', tags='temp')
            self.s = self.s+1

        if self.distance_graph:
            self.distancevalue = (randint(0,100) /2)
            if self.ds == 16:
                # new frame
                self.ds = 1
                self.xx2 = 50
                self.distance_canvas.delete('temp_distance')
            xx1 = self.xx2
            yy1 = self.yy2
            self.xx2 = 50 + self.ds*50
            self.yy2 = 550 - 5 * self.distancevalue
            self.distance_canvas.create_line(xx1, yy1, self.xx2, self.yy2, fill='red', tags='temp_distance')
            self.ds = self.ds+1


        if self.livedata:
            #update InfoCanvas-Dynamic
            self.infocanvas.create_window(70, 80,window=Label(self.infocanvas, text="Current temperature = %d" % (self.tempvalue / 2)))
            self.infocanvas.create_window(60, 100, window=Label(self.infocanvas,text="Current distance = %d" % (self.distancevalue / 2)))
            self.infocanvas.create_window(58, 120, window=Label(self.infocanvas, text="Runtime: %s" % (self.minutes)+" m : %d "%(self.seconds)+"s"))

        self.seconds = self.seconds + 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes = self.minutes + 1

        self.root.after(1000,self.step)

    def temp_graph_window(self):
        #create the canvas for the tempgraph
        self.canvas = Canvas(self.frame, width=810, height=600 ,relief=SUNKEN, bd=1)
        self.canvas.pack(side=LEFT,expand=YES, fill=X)

        #title
        title = Label(self.canvas,text="Temperatuur grafiek",fg='Orange',font=("Arial",16))
        self.canvas.create_window(400,25,window=title)

        # Y-labels
        templabel = Label(self.canvas, text='Temp.', fg='Orange')
        templabel.pack()
        self.canvas.create_window(18, 315, window=templabel)

        celciuslabel = Label(self.canvas, text='In °C', fg='Orange')
        celciuslabel.pack()
        self.canvas.create_window(18, 333, window=celciuslabel)

        # X-labels
        xlabel = Label(self.canvas, text='Tijd in seconden', fg='Orange')
        xlabel.pack()
        self.canvas.create_window(400, 575, window=xlabel)

        self.canvas.create_line(50, 550, 800, 550, width=2)  # x-axis
        self.canvas.create_line(50, 550, 50, 50, width=2)  # y-axis

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

        self.delete_temp = Button(self.canvas, text="X",fg='red', command=lambda: self.delete_canvas())
        self.canvas.create_window(550,25, window=self.delete_temp)

        self.temp_graph = True

    def distance_window(self):
        #create the canvas for the distancegraph
        self.distance_canvas = Canvas(self.frame, width=810, height=600 ,relief=SUNKEN, bd=1)
        self.distance_canvas.pack(side=LEFT,expand=YES, fill=X)

        #title
        title = Label(self.distance_canvas,text="Afstands grafiek",fg='Red',font=("Arial",16))
        self.distance_canvas.create_window(400,25,window=title)

        # Y-labels
        templabel = Label(self.distance_canvas, text=' Afstand', fg='Red')
        templabel.pack()
        self.distance_canvas.create_window(18, 315, window=templabel)

        #celciuslabel = Label(self.distance_canvas, text='In °C', fg='Orange')
        #celciuslabel.pack()
        #self.distance_canvas.create_window(18, 333, window=celciuslabel)

        # X-labels
        xlabel = Label(self.distance_canvas, text='Tijd in seconden', fg='Red')
        xlabel.pack()
        self.distance_canvas.create_window(400, 575, window=xlabel)

        self.distance_canvas.create_line(50, 550, 800, 550, width=2)  # x-axis
        self.distance_canvas.create_line(50, 550, 50, 50, width=2)  # y-axis

        # x-axis
        for i in range(16):
            x = 50 + (i * 50)
            self.distance_canvas.create_line(x,550,x,50, width=1, dash=(2,5))
            self.distance_canvas.create_text(x,550, text='%d'% (i), anchor=N)

        # y-axis
        for i in range(11):
            y = 550 - (i * 50)
            self.distance_canvas.create_line(50,y,800,y, width=1, dash=(2,5))
            self.distance_canvas.create_text(40,y, text='%d'% (i*10/2), anchor=E)

        self.delete_distance = Button(self.distance_canvas, text="X",fg='red', command=self.delete_distancecanvas)
        self.distance_canvas.create_window(550, 25, window=self.delete_distance)

        self.distance_graph = True

    def delete_distancecanvas(self):
        self.distance_canvas.destroy()
        self.distance_graph = False
    def delete_canvas(self):
        self.canvas.destroy()
        self.temp_graph = False
    def delete_livedata(self):
        self.infocanvas.destroy()
        self.livedata = False


    def live_data_window(self):
        #Creates the live data window
        self.infocanvas = Canvas(self.frame,width=300,height=600,relief=SUNKEN, bd=1)
        self.infocanvas.pack(side=RIGHT,expand=YES,fill=X)

        #Infolabels-Static
        self.infocanvas.create_window(150,30,window=Label(self.infocanvas,text="Live Data",font=("Arial",20)))
        self.infocanvas.create_window(55,60,window=Label(self.infocanvas,text="Device ID NO = %s" % (self.sunblind.id)))


        self.delete_livedata = Button(self.infocanvas, text="X",fg='red',command=self.delete_livedata)
        self.infocanvas.create_window(250,20,window=self.delete_livedata)
        self.livedata = True

    def close(self):
        self.root.destroy()


