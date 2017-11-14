# Created on 31 October 2017
# @author Sander Post

# ===============================
# First import al necessary files
# ===============================
import tkinter as tk
from tkinter import *
from threading import Thread
import sys

# Set a global
root = None


class MainView:

    # =========================================
    # Constructor of the class
    # @param model the model we're refering to
    # =========================================
    def __init__(self, model):
        self.model = model
        global root
        root = tk.Tk()
        root.winfo_toplevel().title("Zeng Terminal")

        self.setup_buttons_left()
        if sys.platform.startswith('win'):
            self.show_serials_button()
        self.t1 = Thread(target=self.update, daemon=True)
        self.t1.start()

    def update(self):
        try:
            root.mainloop()
        except:
            pass

    def get_root(self):
        return root

    def show_serials_button(self):
        b1 = Button(self.function_frame_left, text="Show & update COM Ports", width=38, command=self.show_serials)
        b1.grid(row=2, columnspan=2)

    def show_serials(self):
        row = 3
        for i in self.model.serial_ports():
            b1 = Button(self.function_frame_left, text="Add " + str(i), command= lambda: self.model.create_sunblind(root, i))
            b1.grid(row=row, column=0)
            b2 = Button(self.function_frame_left, text="Delete " + str(i), command= lambda: self.model.delete_sunblind(i))
            b2.grid(row=row, column=1)
            row = row + 1

    def setup_buttons_left(self):
        self.function_frame_left = Frame(root)
        self.add_sunblind_button()
        self.del_sunblind_button()
        self.warning()
        self.function_frame_left.pack(side=TOP)

    def new_sunblind(self):
        self.model.create_sunblind(root=root, com="test")

    def del_sunblind(self):
        self.model.delete_sunblind()

    def add_sunblind_button(self):
        button = Button(self.function_frame_left, text="Create new Sunblind Control", command=self.new_sunblind)
        button.grid(row=1,column=0)

    def del_sunblind_button(self):
        button = Button(self.function_frame_left, text="Delete Sunblind", command=self.del_sunblind)
        button.grid(row=1,column=1)

    def warning(self):
        Label(self.function_frame_left, text="!!Do not attach Arduino before running the app on Mac OS!!").grid(row=0, column=0, columnspan=2)
