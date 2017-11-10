# Created on 28 October 2017
# @author Sander Post

# ===============================
# First import al necessary files
# ===============================
from Model import Model
from Mainview import MainView


class Application:
    def __init__(self):
        model = Model()
        model.start_thread()
        MainView(model).update()

# ======================================================
# Try to make this app runnable
#
# Don't attach the Arduino before running your program!
#
# ======================================================

if __name__== '__main__':
    try:
        Application()
    except Exception:
        pass