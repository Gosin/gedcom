import unittest
from output import outputIndiSummary
from output import outputFamSummary
from individual import Individual
from family import Family

class OutputTest(unittest.TestCase):

    def setUp(self):
        self.indi = Individual()
        self.indi.addID('@I2@')
        self.indi.addName('John Rivas')
        self.indi.addSex('M')
        self.indi.addBirt('9 MAY 1978')
        self.indi.addDeat('12 APR 2013')
        self.indi.addFams('@F2@')
        self.indi.addFamc('@F1@')
        
        self.fam1 = Family()
        self.fam1.addFamID('@F2@')
        self.fam1.addHusb('@I2@')
        self.fam1.addWife('@I2@')
        self.fam1.addChil('@I2@')
        self.fam1.addChil('@I2@')

        self.individuals =  dict()
        self.individuals["one"] = self.indi
                
        self.families =  dict()
        self.families["one"] = self.fam1
        
    def test_outputIndiSummary(self):
        outputIndiSummary(self.individuals)

    def test_outputFamSummary(self):
        outputFamSummary(self.families, self.individuals)
        
        
if __name__ == '__main__':
    unittest.main()