class Individual(object):

    def __init__(self):
        self.ID = None
        self.name = None
        self.sex = None
        self.birt = None
        self.deat = None
        self.fams = []
        self.famc = []
  

    def addID(self, ID):
        self.ID = ID
        
    def addName(self, name):
        self.name = name

    def addSex(self, sex):
        if sex == 'M' or sex == 'F':
            self.sex = sex
    
    def addBirt(self, birt):
        self.birt = birt

    def addDeat(self, deat):
        self.deat = deat

    def addFams(self, fams):
        # self.fams = fams
        self.fams.append(fams)

    def addFamc(self, famc):
        # self.famc = famc
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
        return self.deat


    def getFams(self):
        return self.fams

    def getFamc(self):
        return self.famc