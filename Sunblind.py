# Created on 18 October 2017
# @author Groep Zonder Naam

# ===============================
# First import al necessary files
# ===============================

from Sunblindview import SunblindView
from time import sleep
from threading import *
from schedule import Scheduler

class Sunblind:

    # Make some Class variables
    id = 0

    # ========================================
    # Constructor of this class
    # ========================================
    def __init__(self, id, root, model):
        self.rolling_down = False
        self.rolling_up = False
        self.model = model
        self.id = id
        self.view = SunblindView(sunblind=self, root=root, model=model)
        #self.thread_1 = Thread(target=self.check_rolling(), daemon=True)
        #self.thread_1.start()
        #self.check_rolling()
        self.t1 = Thread(target=self.check_rolling, daemon=True)
        self.t1.start()

    def delete_view(self):
        self.view.delete_view()

    def check_rolling(self):
        while True:
            if self.rolling_up == True:
                self.view.going_up(bool=True)
                #self.view.return_frame.update()
                #print(str(self) + " || Rolling Up")
            elif self.rolling_down == True:
                self.view.going_down(True)
                #print(str(self) + " || Rolling down")
            else:
                self.view.going_up(False)
                self.view.going_down(False)
                #print(str(self) + " || Nothing")

    # ========================================
    # Unroll
    # ========================================
    def unroll(self):
        print("unroll")

    # ========================================
    # Roll up
    # ========================================
    def roll_up(self):
        print("Roll Up")

    def set_view(self):
        #SunblindView()
        pass
