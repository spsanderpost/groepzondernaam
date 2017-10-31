# Created on 28 October 2017
# @author Sander Post

# ===============================
# First import al necessary files
# ===============================
import sys
import tkinter as tk
from tkinter import *
from Mainview import MainView


class SunblindView:

    sunblind = ""

    # ===========================
    # The Constructor
    # ===========================
    def __init__(self, sunblind, root):
        self.sunblind = sunblind
        self.return_frame = Frame(master=root, relief=RAISED, bd=2)
        self.setup_board()

    def delete_view(self):
        self.return_frame.forget()


    # ================================
    # Setup the a view for a sunblind
    # TODO: Create entrypoints for controling the sunblinds (Light intensity & maybe warmth?)
    # ================================
    def setup_board(self):
        # Setup specific functions for UI
        def start_go_down(event):
            self.sunblind.rollin_down = True
            #self.status = "Unrolling"
            print("start going down")

        def stop_go_down(event):
            self.sunblind.rollin_down = False
            #self.sunblind.status = "Stopped unrolling"
            print("stop going down")

        def start_go_up(event):
            self.sunblind.rollin_up = True
            #self.sunblind.status = "Rolling up"
            print("start going up")

        def stop_go_up(event):
            self.sunblind.rollin_up = False
            #self.sunblind.status = "Stopped rolling up"
            print("stop going up")

        # Setup some frames to organize
        main_frame = Frame(self.return_frame)
        main_frame.pack(side=LEFT)
        control_frame = Frame(self.return_frame)
        control_frame.pack(side=RIGHT)

        # Setup Up and Down button
        up_path = r"Images/Up.gif"
        down_path = r"Images/Down.gif"
        up_image = PhotoImage(file=up_path).subsample(6)
        down_image = PhotoImage(file=down_path).subsample(6)
        roll_up = Button(control_frame, image=up_image)
        roll_up.image = up_image
        roll_down = Button(control_frame, image=down_image)
        roll_down.image = down_image

        # Create action on Button press and release
        roll_down.bind('<ButtonPress-1>', start_go_down)
        roll_down.bind('<ButtonRelease-1>', stop_go_down)
        roll_up.bind('<ButtonPress-1>', start_go_up)
        roll_up.bind('<ButtonRelease-1>', stop_go_up)


        # Create status label
        status_label = Label(main_frame, text=self.sunblind.id)

        # Create a view that gives me visible action

        led_green_path = r"Images/Green.gif"
        led_yellow_path = r"Images/Yellow.gif"
        led_red_path = r"Images/Red.gif"

        led_green_image = PhotoImage(file=led_green_path).subsample(7)
        led_yellow_image = PhotoImage(file=led_yellow_path).subsample(7)
        led_red_image = PhotoImage(file=led_red_path).subsample(7)

        led_green = Label(main_frame, image=led_green_image)
        led_yellow = Label(main_frame, image=led_yellow_image)
        led_red = Label(main_frame, image=led_red_image)

        led_green.image = led_green_image
        led_yellow.image = led_yellow_image
        led_red.image = led_red_image

        def create_led():
            led_off_path = r"Images/Off.gif"
            led_off_image = PhotoImage(file=led_off_path).subsample(7)
            led_off = Label(main_frame, image=led_off_image)
            led_off.image = led_off_image
            return led_off


        # Bind Buttons to frame
        roll_up.pack()
        roll_down.pack()
        create_led().grid(column=0,row=0)
        create_led().grid(column=1,row=0)
        create_led().grid(column=2,row=0)
        status_label.grid(column=0,row=1, columnspan=3)
        self.return_frame.pack(side=BOTTOM, fill=X, expand=YES)


