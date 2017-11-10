# Created on 18 October 2017
# @author Groep Zonder Naam

# ===============================
# First import al necessary files
# ===============================

from Sunblindview import SunblindView
from SettingsView import SettingsView
from threading import *
from time import sleep
import serial

class Sunblind:

    # Make some Class variables
    is_alive = False
    com = 0

    # ========================================
    # Constructor of this class
    # ========================================
    def __init__(self, com, model, root):
        self.max_roll_out = 0
        self.min_roll_out = 0
        self.root = root
        self.is_alive = True
        self.rolling_down = False
        self.rolling_up = False
        self.model = model
        self.com = com
        self.view = SunblindView(sunblind=self, model=model, root=root)
        self.serial = serial.Serial(com, 9600, timeout=.1)
        t1 = Thread(target=self.check_rolling, daemon=True)
        t2 = Thread(target=self.getSerialData, daemon=True)
        t1.start()
        t2.start()

    def delete_view(self):
        self.view.delete_view()

    def set_sunblind_settings(self):
        SettingsView(self, self.model).root.mainloop()

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

    def write_roll_to_arduino(self, what, val):
        sleep(1)
        if what == min:
            self.serial.write("SETMIN" + val)
        elif what == max:
            self.serial.write("SETMAX" + val)

    def unroll(self):
        print("unroll")

    def roll_up(self):
        print("Roll Up")

    def set_view(self):
        #SunblindView()
        pass

    def getSerialData(self):
        ser = serial.Serial(self.com, 9600, timeout=1)
        lastval = ""
        last = ""
        sensor_name = ""
        output_dictionary = {}
        output_dictionary['Poort'] = self.com
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
            print(output_dictionary)