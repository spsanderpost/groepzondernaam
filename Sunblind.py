# Created on 18 October 2017
# @author Groep Zonder Naam

# ===============================
# First import al necessary files
# ===============================

from Sunblindview import SunblindView
from time import sleep
from threading import *
from schedule import Scheduler
import serial

class Sunblind:

    # Make some Class variables
    is_alive = False
    com = 0
    max_roll_out = 160

    # ========================================
    # Constructor of this class
    # ========================================
    def __init__(self, com, model, root):
        self.root = root
        self.is_alive = True
        self.rolling_down = False
        self.rolling_up = False
        self.model = model
        self.com = com
        self.view = SunblindView(sunblind=self, model=model, root=root)
        #self.thread_1 = Thread(target=self.check_rolling(), daemon=True)
        #self.thread_1.start()
        #self.check_rolling()
        self.t1 = Thread(target=self.check_rolling, daemon=True)
        self.t1.start()

    def delete_view(self):
        self.view.delete_view()

    def check_rolling(self):
        initial_roll_out = i = 0
        while self.is_alive == True:
            if self.rolling_up == True:
                self.view.going_up(bool=True)
                if i >= 10:

                    self.view.draw(i)
                    i = i - 5
                else:
                    pass
            elif self.rolling_down == True:
                self.view.going_down(True)
                if i <= self.max_roll_out:
                    i += 5
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

# argument is com-poort.
    def getSerialData(port):
        ser = serial.Serial(port, 9600, timeout=1)
        lastval = ""
        last = ""
        sensor_name = ""
        output_dictionary = {}
        output_dictionary['Poort'] = port
        while True:
            data = ser.read()
            data = str(data, 'utf-8')
            if (data is "L" or data is "C" or data is "D"):
                last = data
            elif (data is "X"):
                if (last is "D"):
                    sensor_name = "Afstand"
                elif (last is "L"):
                    sensor_name = "Licht"
                elif (last is "C"):
                    sensor_name = "Temperatuur"
                    # print(sensor_name, lastval)
                output_dictionary[sensor_name] = int(lastval)
                print(output_dictionary)
                lastval = ""
            else:
                lastval += data.rstrip()