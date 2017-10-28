# Created on 28 October 2017
# @author Sander Post

# ===============================
# First import al necessary files
# ===============================
import sys
import tkinter as tk
from tkinter import *


class Mainview:

    # ===========================
    # The Constructor
    # ===========================
    def __init__(self, model):
        self.model = model
        self.root = tk.Tk()
        self.root.winfo_toplevel().title("Zeng Terminal")
        self.setup_board()

    # ===========================
    # Setup the main window
    # ===========================
    def setup_board(self):
        # Setup specific functions for UI
        def start_go_down(event):
            self.model.rollin_down = True
            print("Unrolling")
        def stop_go_down(event):
            self.model.rollin_down = False
            self.model.status = "Stopped unrolling"
        def start_go_up(event):
            self.model.rollin_up = True
            print("Rolling up")
        def stop_go_up(event):
            self.model.rollin_up = False
            self.model.status = "Stopped rolling up"


        # Setup some frames to organize
        space = LabelFrame()
        main_frame = Frame(space)
        main_frame.pack(side=TOP)
        control_frame = Frame(self.root)
        control_frame.pack(side=RIGHT, fill=Y, expand=YES)
        terminal_frame = Frame(self.root)
        terminal_frame.pack(side=BOTTOM, fill=X, expand=YES)
        # Pack some space into the frame
        space.pack(fill=BOTH, expand=YES)

        # Setup Up and Down button
        up_path = r"Images/Up.gif"
        down_path = r"Images/Down.gif"
        up_image = PhotoImage(file=up_path).subsample(3)
        down_image = PhotoImage(file=down_path).subsample(3)
        roll_up = Button(control_frame, image=up_image)
        roll_up.image = up_image
        roll_down = Button(control_frame, image=down_image)
        roll_down.image = down_image

        # Create action on Button press and release
        roll_up.bind('<ButtonPress-1>',start_go_up)
        roll_up.bind('<ButtonRelease-1>',stop_go_up)
        roll_down.bind('<ButtonPress-1>',start_go_down)
        roll_down.bind('<ButtonRelease-1>',stop_go_down)

        # Create status label
        status_label = Label(terminal_frame, text="Later on we'll create an responsive label, which will give us an continious status!")

        # Create a view that gives me visible action

        led_green_path = r"Images/Green.gif"
        led_yellow_path = r"Images/Yellow.gif"
        led_red_path = r"Images/Red.gif"

        led_green_image = PhotoImage(file=led_green_path).subsample(2)
        led_yellow_image = PhotoImage(file=led_yellow_path).subsample(2)
        led_red_image = PhotoImage(file=led_red_path).subsample(2)


        led_green = Label(main_frame, image=led_green_image)
        led_yellow = Label(main_frame, image=led_yellow_image)
        led_red = Label(main_frame, image=led_red_image)

        led_green.image = led_green_image
        led_yellow.image = led_yellow_image
        led_red.image = led_red_image

        def create_led():
            led_off_path = r"Images/Off.gif"
            led_off_image = PhotoImage(file=led_off_path).subsample(3)
            led_off = Label(main_frame, image=led_off_image)
            led_off.image = led_off_image
            return led_off


        # Bind Buttons to frame
        roll_up.pack()
        roll_down.pack()

        create_led().pack(side=LEFT)
        create_led().pack(side=LEFT)
        create_led().pack(side=LEFT)

        status_label.pack()
