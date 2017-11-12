# Created on 31 October 2017
# @author Sander Post

# ===============================
# First import al necessary files
# ===============================
from Sunblind import Sunblind
from threading import Thread
from Mainview import root
import serial
import sys
import glob
from time import *


class Model:

    sunblinds = []

    # ============================
    # Constructor
    # ============================
    def __init__(self):
        #self.coms = self.serial_ports()
        self.com_list = []
        self.counter = 0
        pass

    def start_thread(self):
        t1 = Thread(target=self.com_check, daemon=True)
        t1.start()

    # This function first checks for os
    # Then it adds or deletes sunblinds when adding one to a COM port
    def com_check(self):
        while True:
            sleep(0.5)
            if sys.platform.startswith('win'):
                current = self.serial_ports()
                sleep(0.5)
                for i in current:
                    if i not in self.com_list:
                        self.com_list.append(i)
                        self.create_sunblind(root,i)
                print(current)
                print(self.com_list)

                if current != self.com_list:
                    for i in self.com_list:
                        if i not in current:
                            self.com_list.remove(i)
                            self.delete_sunblind(i)

            elif sys.platform.startswith('darwin'):
                current = self.serial_ports()
                diffadd = [item for item in current if not item in self.coms]
                diffdel = [item for item in self.coms if not item in current]
                if len(diffadd) != 0:
                    for x in diffadd:
                        if x not in self.coms:
                            self.create_sunblind(root=root, com=x)
                            self.coms = current
                elif len(diffdel) != 0:
                    for x in diffdel:
                        self.delete_sunblind(com=x)
                        self.coms = current
            else:
                raise EnvironmentError

    # Create a sunblind
    # @param root is the window where a view has to be attached
    # @param com is the port where an Arduino is connected to and an identifier in the object
    def create_sunblind(self, root, com):
        if com != "test":
            com = com
        else:
            com = "test"

        sunblind = Sunblind(com=com, model=self, root=root)
        self.sunblinds.append(sunblind)
    """
    def delete_sunblind(self, com=None):
        for x in self.sunblinds:
            x.delete_view()
            x.is_alive = False
            del x
    """


    # Delete a sunblind
    # @param com when not given None else the exact port where an Arduino is connected to
    def delete_sunblind(self, com=None):
        for x in self.sunblinds:
            if x.com == com:
                x.delete_view()
                x.is_alive = False
                del x
            elif x.com == "test":
                x.delete_view()
                x.is_alive = False
                del x


    def get_sunblind(self, id):
        return self.sunblinds[id]

    # Gets a list with added ports to the system
    # First checks what platform where wunning
    def serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result