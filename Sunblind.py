# Created on 18 October 2017
# @author Groep Zonder Naam

# ===============================
# First import al necessary files
# ===============================

from Sunblindview import SunblindView
from time import sleep
from threading import *
from GraphView import *

class Sunblind:

    # Make some Class variables
    id = 0
    max_roll_out = 160

    # ========================================
    # Constructor of this class
    # ========================================
    def __init__(self, id, root, model):
        self.rolling_down = False
        self.rolling_up = False
        self.live_data = False
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
        initial_roll_out = i = 0
        while True:
            if self.rolling_up == True:
                self.view.going_up(bool=True)
                if i >= 10:

                    self.view.draw(i)
                    i = i - 10
                else:
                    pass
            elif self.rolling_down == True:
                self.view.going_down(True)
                if i <= self.max_roll_out:
                    i += 10
                    self.view.draw(i)

                else:
                    pass
            else:
                self.view.going_up(False)
                self.view.going_down(False)

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
