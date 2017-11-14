# Created on 10 November 2017
# @author Sander Post

# ===============================
# First import al necessary files
# ===============================
import tkinter as tk
from tkinter import *


class SettingsView:

    # =============================================
    # Constructor
    # @param sunblind the object we're refering to
    # @param model the model were refering to
    # =============================================
    def __init__(self, sunblind, model):
        self.sunblind = sunblind
        self.model = model
        self.root = tk.Tk()
        self.root.winfo_toplevel().title("Sunblind settings")
        self.set_settings()

    def set_settings(self):
        l1 = Label(self.root, text="Max Outroll: ")
        l2 = Label(self.root, text="Min Outroll: ")
        self.e1 = Entry(self.root, width=60)
        self.e2 = Entry(self.root, width=60)
        self.e1.insert(1, self.sunblind.max_roll_out)
        self.e2.insert(1, self.sunblind.min_roll_out)
        l1.grid(row=0, column=0)
        l2.grid(row=1, column=0)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        b1 = Button(self.root, text="Save", command=self.save)
        b1.grid(row=2, column=1)

    def save(self):
        valuemax = self.e1.get() / 10
        valuemin = self.e2.get() / 10
        try:
            self.sunblind.max_roll_out = int(valuemax)
            self.sunblind.min_roll_out = int(valuemin)
            self.sunblind.write_roll_to_arduino(what=max, val=valuemax)
            self.sunblind.write_roll_to_arduino(what=min, val=valuemin)
        except ValueError:
            print("Geen juiste waarden ingevoerd.")