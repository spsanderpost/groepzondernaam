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
        model = Model()
        MainView(model).update()
        pass

    def test(self):
        self.view.update()

    def main(self):
        self.test()

# ===============================
# Try to make this app runnable
# ===============================

if __name__== '__main__':
    try:
        Application()
    except KeyboardInterrupt:
        pass