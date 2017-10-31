# Created on 28 October 2017
# @author Sander Post

# ===============================
# First import al necessary files
# ===============================

from Model import Model
from Sunblind import Sunblind
from Mainview import MainView
from Sunblindview import SunblindView
from threading import Thread
import tkinter as tk

class Application():
    def __init__(self):
        pass

    model = Model()
    view = MainView(model)

    def test(self):
        self.view.update()

    # =====================================
    # If main gets called start all threads
    # =====================================
    def main(self):
        self.test()

# ===============================
# Try to make this app runnable
# ===============================

if __name__== '__main__':
    try:
        Application().main()
    except KeyboardInterrupt:
        pass