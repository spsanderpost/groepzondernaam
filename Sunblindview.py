# Created on 28 October 2017
# @author Sander Post

# ===============================
# First import al necessary files
# ===============================
import sys
import tkinter as tk
from tkinter import *
from Mainview import MainView
from time import sleep
from threading import Thread


class SunblindView:

    id = ""

    # ===========================
    # The Constructor
    # ===========================
    def __init__(self, sunblind, model, root):
        self.model = model
        self.sunblind = sunblind
        self.return_frame = Frame(master=root, relief=RAISED, bd=2)

        self.main_frame = Frame(master=self.return_frame)
        self.main_frame.pack(side=LEFT)
        self.control_frame = Frame(master=self.return_frame)
        self.control_frame.pack(side=RIGHT)

        self.create_buttons()
        self.give_me_leds()
        self.return_frame.pack(side=BOTTOM, fill=X, expand=YES)

    def delete_view(self):
        self.return_frame.forget()

    def create_some(self, return_frame):
        c = Canvas(return_frame)
        # feest = 0
        # self.c.create_rectangle(10, 10, 100, feest, width=3)
        pass

    def create_led(self, state):
        if state == "off":
            led_off_path = r"Images/Off.gif"
            led_off_image = PhotoImage(file=led_off_path).subsample(9)
            led_off = Label(self.main_frame, image=led_off_image)
            led_off.image = led_off_image
            return led_off
        elif state == "green":
            led_green_path = r"Images/Green.gif"
            led_green_image = PhotoImage(file=led_green_path).subsample(9)
            led_green = Label(self.main_frame, image=led_green_image)
            led_green.image = led_green_image
            return led_green
        elif state == "yellow":
            led_yellow_path = r"Images/Yellow.gif"
            led_yellow_image = PhotoImage(file=led_yellow_path).subsample(9)
            led_yellow = Label(self.main_frame, image=led_yellow_image)
            led_yellow.image = led_yellow_image
            return led_yellow
        elif state == "red":
            led_red_path = r"Images/Red.gif"
            led_red_image = PhotoImage(file=led_red_path).subsample(9)
            led_red = Label(self.main_frame, image=led_red_image)
            led_red.image = led_red_image
            return led_red

    def give_me_leds(self):
        for x in range(3):
            self.create_led("off")
            self.create_led("off").grid(column=x, row=0)
            self.return_frame.update()

    def going_up(self, bool):
        if bool == True:
            working = True
            green = self.create_led("green")
            green.grid(column=0, row=0)
            sleep(0.5)
            green.destroy()
            sleep(0.5)
        elif bool == False:
            working = False

    def going_down(self, bool):
        if bool == True:
            working = True
            red = self.create_led("red")
            red.grid(column=1, row=0)
            sleep(0.5)
            red.destroy()
            sleep(0.5)
        elif bool == False:
            working = False

    def start_go_up(self, event):
        self.sunblind.rolling_up = True
        #self.sunblind.status = "Rolling up"
        #print("start going up")

    def stop_go_up(self, event):
        self.sunblind.rolling_up = False
        #self.sunblind.status = "Stopped rolling up"
        #print("stop going up")

    def start_go_down(self, event):
        self.sunblind.rolling_down = True
        #self.status = "Unrolling"
        #print(self.model.rollin_down)

    def stop_go_down(self, event):
        self.sunblind.rolling_down = False
        #self.sunblind.status = "Stopped unrolling"
        #print("stop going down")

    def create_buttons(self):
        # Setup Up and Down button
        up_path = r"Images/Up.gif"
        down_path = r"Images/Down.gif"
        up_image = PhotoImage(file=up_path).subsample(6)
        down_image = PhotoImage(file=down_path).subsample(6)
        roll_up = Button(self.control_frame, image=up_image)
        roll_up.image = up_image
        roll_down = Button(self.control_frame, image=down_image)
        roll_down.image = down_image

        # Create action on Button press and release
        roll_up.bind('<ButtonPress-1>',     self.start_go_up)
        roll_up.bind('<ButtonRelease-1>',   self.stop_go_up)
        roll_down.bind('<ButtonPress-1>',   self.start_go_down)
        roll_down.bind('<ButtonRelease-1>', self.stop_go_down)

        roll_up.pack()
        roll_down.pack()

    def initiate_lights(self):
        # Create a view that gives me visible action
        pass


