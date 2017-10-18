'''
Created on 18 October 2017
@author Groep Zonder Naam
'''

class Model():

    # Make some Class variables
    # Onder andere de maximale uitrol stand
    # Dit is tevens en te plotten as
    MAX_UITROL = 160
    uitrol = 160
    breedte = 0
    status = ""

    #========================================
    # Constructor van de klasse model.
    #========================================
    #def __init__(self):


    # =======================================
    # Rol het luik op.
    # =======================================
    def rol_op(self):
        while self.uitrol > 0:
            if self.uitrol > 0:
                self.uitrol -= 1
                self.status = "Wordt opgerold"
                print(self.status+" / "+str(self.uitrol))
            elif self.uitrol == 0:
                self.status = "Is al opgerold"
                print(self.status + " / " + str(self.uitrol))

    # =======================================
    # Constructor van de klasse model.
    # =======================================
    def rol_uit(self):
        if self.uitrol <= self.uitrol:
            self.uitrol += 1
            self.status = "Wordt uitgerold"
        elif self.uitrol == self.MAX_UITROL:
            self.status = "Is al uitgerold"

model = Model()
model.rol_op()