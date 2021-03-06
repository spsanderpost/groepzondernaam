# Created on 28 October 2017
# @author Sander Post

# ===============================
# First import al necessary files
# ===============================
from tkinter import *
from time import sleep
from GraphView import *

class SunblindView:

    # ===========================
    # The Constructor
    # ===========================
    def __init__(self, sunblind, model, root):
        self.root = root
        self.model = model
        self.sunblind = sunblind
        self.return_frame = Frame(master=self.root, relief=RAISED, bd=2)
        self.main_frame = Frame(master=self.return_frame)
        self.main_frame.pack(side=LEFT)
        self.control_frame = Frame(master=self.return_frame)
        self.control_frame.pack(side=RIGHT)
        self.create_buttons()
        self.give_me_leds()
        #self.canvas = Canvas(self.main_frame, width=110, height=170, relief=SUNKEN, bd=1)
        #self.canvas.grid(column=4,row=0)
        self.return_frame.pack(side=BOTTOM, fill=X, expand=YES)

    def delete_view(self):
        self.return_frame.forget()

    def draw_canvas(self):
        self.canvas = Canvas(self.main_frame, width=110, height=self.sunblind.output_dictionary["Max"], relief=SUNKEN, bd=1)
        self.canvas.grid(column=4,row=0)

    # Draw a virtual sunscreen in a window
    # @param state is how much the screen has unrolled
    def draw(self, state):
        self.canvas.create_rectangle(10, 10, 110, state, fill="grey")
        for x in self.canvas.find_all():
            self.canvas.delete(x-1)
        self.canvas.update()

    # Draw some light on the screen
    # @param state which color we wanna draw
    def create_led(self, state):
        if state == "off":
            led_off_path = r"Images/Small Off.gif"
            led_off_image = PhotoImage(file=led_off_path)
            led_off = Label(self.main_frame, image=led_off_image)
            led_off.image = led_off_image
            return led_off
        elif state == "green":
            led_green_path = r"Images/Small Green.gif"
            led_green_image = PhotoImage(file=led_green_path)
            led_green = Label(self.main_frame, image=led_green_image)
            led_green.image = led_green_image
            return led_green
        elif state == "yellow":
            led_yellow_path = r"Images/Small Yellow.gif"
            led_yellow_image = PhotoImage(file=led_yellow_path)
            led_yellow = Label(self.main_frame, image=led_yellow_image)
            led_yellow.image = led_yellow_image
            return led_yellow
        elif state == "red":
            led_red_path = r"Images/Small Red.gif"
            led_red_image = PhotoImage(file=led_red_path)
            led_red = Label(self.main_frame, image=led_red_image)
            led_red.image = led_red_image
            return led_red

    def give_me_leds(self):
        for x in range(3):
            self.create_led("off")
            self.create_led("off").grid(column=x, row=0)
            self.return_frame.update()

    def status_light(self):
        self.yellow = self.create_led("yellow")
        self.yellow.grid(column=2, row=0)

    def off_status_light(self):
        self.yellow.destroy()
        self.return_frame.update()


    def going_up(self, bool):
        if bool == True:
            green = self.create_led("green")
            green.grid(column=0, row=0)
            sleep(0.5)
            green.destroy()
            self.return_frame.update()
            sleep(0.5)

        elif bool == False:
            pass

    def going_down(self, bool):
        if bool == True:
            red = self.create_led("red")
            red.grid(column=1, row=0)
            sleep(0.5)
            red.destroy()
            self.return_frame.update()
            sleep(0.5)

        elif bool == False:
            pass

    def start_go_up(self, event):
        self.sunblind.rolling_up = True
        self.status_light()

    def stop_go_up(self, event):
        self.sunblind.rolling_up = False
        self.off_status_light()

    def start_go_down(self, event):
        self.sunblind.rolling_down = True
        self.status_light()

    def stop_go_down(self, event):
        self.sunblind.rolling_down = False
        self.off_status_light()
    def enable_live_data(self):
        self.graphview = GraphView(sunblind=self.sunblind, model=self.model)

    def create_buttons(self):
        # Setup Up and Down button
        up_path = r"Images/Small Up.gif"
        down_path = r"Images/Small Down.gif"
        up_image = PhotoImage(file=up_path)
        down_image = PhotoImage(file=down_path)
        roll_up = Button(self.control_frame, image=up_image)
        roll_up.image = up_image
        roll_down = Button(self.control_frame, image=down_image)
        roll_down.image = down_image
        einstellungen_path = r"Images/Settings.gif"
        einstellungen_image = PhotoImage(file=einstellungen_path).subsample(2)
        einstellungen = Button(self.control_frame, text="Settings...", image=einstellungen_image, command=self.sunblind.set_sunblind_settings)
        einstellungen.image = einstellungen_image

        graph_path = r"Images/Graphs.gif"
        graph_image = PhotoImage(file=graph_path).subsample(2)
        graphbutton = Button(self.control_frame, text="Grafiek", image=graph_image, command=self.enable_live_data)
        graphbutton.image = graph_image

        # Create action on Button press and release
        roll_up.bind('<ButtonPress-1>',     self.start_go_up)
        roll_up.bind('<ButtonRelease-1>',   self.stop_go_up)
        roll_down.bind('<ButtonPress-1>',   self.start_go_down)
        roll_down.bind('<ButtonRelease-1>', self.stop_go_down)

        roll_up.pack()
        roll_down.pack()
        einstellungen.pack()
        graphbutton.pack()



