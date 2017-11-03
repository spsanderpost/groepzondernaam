# Created on 31 October 2017
# @author Sander Post

# ===============================
# First import al necessary files
# ===============================

from Sunblind import Sunblind

class Model:

    sunblinds = []

    def __init__(self):
        pass

    def create_sunblind(self, root):

        if len(self.sunblinds) == 0:
            id = 0
        else: id = int(len(self.sunblinds))

        sunblind = Sunblind(id=id, root=root, model=self)

        self.sunblinds.append(sunblind)

    def delete_sunblind(self):
        current = self.sunblinds.pop()
        current.delete_view()
        del current

    def get_sunblind(self, id):
        return self.sunblinds[id]
