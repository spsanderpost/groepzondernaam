# Created on 31 October 2017
# @author Sander Post

# ===============================
# First import al necessary files
# ===============================
import tkinter as tk
from tkinter import *
from threading import Thread


root = None


class MainView:

    # ===========================
    # Constructor of the class
    # ===========================
    def __init__(self, model):
        self.model = model
        global root
        root = tk.Tk()
        root.winfo_toplevel().title("Zeng Terminal")
        self.setup_buttons_left()
        self.t1 = Thread(target=self.update, daemon=True)
        self.t1.start()

    def update(self):
        try:
            root.mainloop()
        except:
            pass

    def get_root(self):
        return root

    def setup_buttons_left(self):
        self.function_frame_left = Frame(root)
        self.add_sunblind_button()
        self.del_sunblind_button()
        self.function_frame_left.pack(side=TOP)

    def new_sunblind(self):
        self.model.create_sunblind(root=root, com="test")

    def del_sunblind(self):
        self.model.delete_sunblind()

    def add_sunblind_button(self):
        button = Button(self.function_frame_left, text="Create new Sunblind Control", command=self.new_sunblind)
        button.grid(row=0,column=0)

    def del_sunblind_button(self):
        button = Button(self.function_frame_left, text="Delete Sunblind", command=self.del_sunblind)
        button.grid(row=0,column=1)



