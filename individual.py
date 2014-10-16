class Individual(object):

    def __init__(self):
        self.ID = ''
        self.name = ''
        self.sex = ''
        self.birt = ''
        self.deat = ''
        self.fams = []
        self.famc = []


    def addID(self, ID):
        self.ID = ID

    def addName(self, name):
        self.name = name

    def addSex(self, sex):
        if sex == 'M' or sex == 'F':
            self.sex = sex
        else:
            print "Invalid sex value."

    def addBirt(self, birt):
        self.birt = birt

    def addDeat(self, deat):
        self.deat = deat

    def addFams(self, fams):
        self.fams.append(fams)

    def addFamc(self, famc):
        self.famc.append(famc)

    def getID(self):
        return self.ID

    def getSex(self):
        return self.sex

    def getName(self):
        return self.name

    def getBirt(self):
        return self.birt

    def getDeat(self):
        if self.deat:
            return self.deat
        else:
            print "No death date available."

    def getFams(self):
        return self.fams

    def getFamc(self):
        return self.famc