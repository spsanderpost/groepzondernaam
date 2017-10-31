# Created on 18 October 2017
# @author Groep Zonder Naam

# ===============================
# First import al necessary files
# ===============================

from Sunblindview import SunblindView
from time import sleep
from threading import Thread

class Sunblind:

    # Make some Class variables
    id = 0

    max_unroll = 160
    current_unroll = 0
    width = 0

    rolling_down = False
    rolling_up = False
    status = ""

    # ========================================
    # Constructor of this class
    # ========================================
    def __init__(self, id, root):
        self.id = id
        self.view = SunblindView(sunblind=self, root=root)
        #self.thread_1 = Thread(target=self.check_rolling(), daemon=True)
        #self.thread_1.start()
        #self.check_rolling()
        self.t1 = Thread(target=self.check_rolling)
        self.t1.start()

    def __del__(self):
        print("Gone!")

    def lock_thread(self):
        try:
            del self.t1
        except:
            pass

    def delete_view(self):
        self.view.delete_view()

    def check_rolling(self):
        while self.rolling_up == True:
            print("rolling up")
        while self.rolling_up == False:
            pass
        while self.rolling_down == True:
            pass
        while self.rolling_down == False:
            pass
        sleep(1)

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
