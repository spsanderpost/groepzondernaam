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
import copy

class Model:

    sunblinds = []

    def __init__(self):
        self.com_list = []
        self.counter = 0
        self.current = []
        self.com_delete = []
        pass

    def start_thread(self):
        t1 = Thread(target=self.com_check, daemon=True)
        t1.start()

    def com_check(self):
        while True:
            sleep(1)
            current = self.serial_ports()
            for i in current:
                if i not in self.com_list:
                    x = i[3:4]
                    self.com_list.append(i)
                    self.create_sunblind(root,com=x)
            if current != self.com_list:
                for i in self.com_list:
                    if i not in current:
                        x = copy.copy(i)
                        self.com_list.remove(i)
                        self.delete_sunblind(com=x)

    def create_sunblind(self, root, com):
        if com != "test":
            com = "COM"+com
        else:
            com = "test"
        print(com)
        sunblind = Sunblind(com=com, model=self, root=root)
        self.sunblinds.append(sunblind)

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

    # get list met serial poorten
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
