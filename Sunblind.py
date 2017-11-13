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
    com = ""

    # ==========================================================
    # Constructor of this class
    # @param com the com port where the object has to attach to
    # @param model the standard model
    # @param root the window where views has to attach to
    # ==========================================================
    def __init__(self, com, model, root):
        self.output_dictionary = {"Afstand": 0, "Licht": 0, "Temperatuur": 0, "Min": 0, "Max": 0}
        self.Afstand = 0
        self.Licht = 0
        self.Temperatuur = 0
        self.Max = 160
        self.Min = 0
        self.root = root
        self.is_alive = True
        self.rolling_down = False
        self.rolling_up = False
        self.model = model
        self.com = com
        self.view = SunblindView(sunblind=self, model=model, root=root)
        self.start_reading()
        t1 = Thread(target=self.check_rolling, daemon=True)
        t1.start()

    def start_reading(self):
        if self.com != "test":
            self.serial = serial.Serial(self.com, 9600, timeout=2, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS) #parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS
            t2 = Thread(target=self.getSerialData, daemon=True)
            t2.start()
        else:
            pass

    def delete_view(self):
        if self.com != "test":
            try:
                pass
                self.serial.close()
            except:
                print("Failed to close COM-Connection")
        self.view.delete_view()

    # Open a settings window
    def set_sunblind_settings(self):
        SettingsView(self, self.model).root.mainloop()

    # First threading method
    # Check for adjustments in variables in this class
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

    # Write some things to Arduino
    # @param what what vaiable we want to write, kind a case function
    # @val what value we want to write
    def write_roll_to_arduino(self, what, val=None):
        sleep(1)
        if what == min:
            self.serial.write(("I" + val+"X").encode())
        elif what == max:
            self.serial.write(("I" + val+"Z").encode())
        elif what == "up":
            self.serial.write(("B").encode())
        elif what == "down":
            self.serial.write(("F").encode())
        elif what == "stop":
            self.serial.write(("S").encode())

    # Some useless print method
    def unroll(self):
        print("unroll")

    # Another useless print method
    def roll_up(self):
        print("Roll Up")

    def set_values(self):
        self.min_roll_out = self.dictionary["Min"]
        self.max_roll_out = self.dictionary["Max"]

    # Second threading method
    # Here we're reading the data send from the Arduino
    def getSerialData(self):
        lastval = ""
        last = ""
        sensor_name = ""
        self.output_dictionary['Poort'] = self.com
        print(self.output_dictionary)
        while self.is_alive:
            try:
                data = self.serial.read()
                data = str(data, 'utf-8')
                #print(data)
                if (data is "L" or data is "C" or data is "D" or data is "M" or data is "U"):
                    last = data
                elif (data is "X"):
                    if (last is "D"):
                        sensor_name = "Afstand"
                    elif (last is "L"):
                        sensor_name = "Licht"
                    elif (last is "C"):
                        sensor_name = "Temperatuur"
                    elif (last is "M"):
                        sensor_name = "Min"
                    elif (last is "U"):
                        sensor_name = "Max"
                    self.output_dictionary[sensor_name] = int(lastval)
                    lastval = ""
                else:
                    lastval += data.rstrip()
                self.set_values()
            except Exception:
                pass
            print(self.output_dictionary)