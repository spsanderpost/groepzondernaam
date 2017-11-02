# Created on 31 October 2017
# @author Sander Post

# ===============================
# First import al necessary files
# ===============================

import tkinter as tk
from tkinter import *
from threading import Thread
from time import sleep

class MainView:

    # ===========================
    # Constructor of the class
    # ===========================
    def __init__(self, model):
        self.model = model
        self.root = tk.Tk()
        self.root.winfo_toplevel().title("Zeng Terminal")
        self.setup_buttons_left()
        self.t1 = Thread(target=self.update, daemon=True)
        self.t1.start()

    def update(self):
        try:
            self.root.mainloop()
        except:
            pass

    def setup_buttons_left(self):
        self.function_frame_left = Frame(self.root)
        self.add_sunblind_button()
        self.del_sunblind_button()
        self.function_frame_left.pack(side=TOP)

    def new_sunblind(self):
        self.model.create_sunblind(root=self.root)
        #Tk.update(self.root)

    def del_sunblind(self):
        self.model.delete_sunblind()
        #Tk.update(self.root)

    def add_sunblind_button(self):
        button = Button(self.function_frame_left, text="Create new Sunblind Control", command=self.new_sunblind)
        button.grid(row=0,column=0)
        #Tk.update(self.root)

    def del_sunblind_button(self):
        button = Button(self.function_frame_left, text="Delete Sunblind", command=self.del_sunblind)
        button.grid(row=0,column=1)



