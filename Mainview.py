# Created on 28 October 2017
# @author Sander Post

# ===============================
# First import al necessary files
# ===============================
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

        # Setup some frames to organize
        main_frame = Frame(self.root)
        main_frame.pack(side=TOP)
        control_frame = Frame(self.root)
        control_frame.pack(side=RIGHT)
        terminal_frame = Frame(self.root)
        terminal_frame.pack(side=BOTTOM)
