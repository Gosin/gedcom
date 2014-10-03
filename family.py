class Family(object):

    def __init__(self):
        self.fam_id = ''
        self.husb = ''
        self.wife = ''
        self.marr = ''
        self.div = ''
        self.chil = []

    def addFamID(self, fam_id):
        self.fam_id = fam_id

    def addHusb(self, husb):
        self.husb = husb

    def addWife(self, wife):
        self.wife = wife

    def addMarr(self, marr):
        self.marr = marr

    def addDiv(self, div):
        self.div = div

    def addChil(self, chil):
        self.chil.append(chil)

    def getFamID(self):
        return self.fam_id

    def getHusb(self):
        return self.husb

    def getWife(self):
        return self.wife

    def getChil(self):
        return self.chil

    def getMarr(self):
        return self.marr

    def getDiv(self):
        if self.div:
            return self.div
        else:
            print "Divorce Date not available."

    def getChild(self):
        return self.chil