import tkinter as tk
from tkinter import *

class SettingsView:
    def __init__(self, sunblind, model):
        self.sunblind = sunblind
        self.model = model
        self.root = tk.Tk()
        self.set_settings()

    def set_settings(self):
        l1 = Label(self.root, text="Max Outroll: ")
        l2 = Label(self.root, text="Min Outroll: ")
        self.e1 = Entry(self.root, width=60)
        self.e2 = Entry(self.root, width=60)
        l1.grid(row=0, column=0)
        l2.grid(row=1, column=0)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)

        b1 = Button(self.root, text="Save", command=self.save)
        b1.grid(row=2, column=1)

    def save(self):
        valuemax = self.e1.get()
        valuemin = self.e2.get()
        try:
            self.sunblind.max_roll_out = int(valuemax)
            self.sunblind.min_roll_out = int(valuemin)
            self.sunblind.write_roll_to_arduino(what=max, val=valuemax)
            self.sunblind.write_roll_to_arduino(what=min, val=valuemin)
        except ValueError:
            print("Geen waarde jong!")