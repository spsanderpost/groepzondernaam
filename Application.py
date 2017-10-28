# Created on 28 October 2017
# @author Sander Post

# ===============================
# First import al necessary files
# ===============================

from Model import Model
from Mainview import Mainview
from threading import Thread

class Application:
    def __init__(self):
        pass

    model = Model()

    # =====================================
    # Main window in a thread
    # =====================================
    def window_in_a_thread(self):
        window = Mainview(self.model).root.mainloop()

    # =====================================
    # If main gets called start all threads
    # =====================================
    def main(self):
        # t1 = Thread(target=, daemon=True)
        # t1.start()
        self.window_in_a_thread()

# ===============================
# Try to make this app runnable
# ===============================

if __name__== '__main__':
    try:
        Application().main()
    except KeyboardInterrupt:
        pass