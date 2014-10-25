import unittest
from family import Family
from individual import Individual
from AnomalyCheck import checkSameHusbWife
from AnomalyCheck import checkDeathBeforeBirth


class GedcomTest(unittest.TestCase):
    def setUp(self):
        self.indi = Individual()
        self.indi.addID('@I2@')
        self.indi.addName('John Rivas')
        self.indi.addSex('M')
        self.indi.addBirt('9 MAY 1978')
        self.indi.addDeat('12 APR 2013')

        
        self.fam1 = Family()
        self.fam1.addFamID('@F2@')
        self.fam1.addHusb('@I1@')
        self.fam1.addWife('@I2@')
        self.fam1.addChil('@I4@')
        self.fam1.addChil('@I5@')
        self.fam1.addMarr('5 OCT 1999')
        self.fam1.addDiv('12 JUN 2012')
        self.fam2 = Family()
        self.fam2.addFamID('@F3@')
        self.fam2.addHusb('@I3@')
        self.fam2.addWife('@I3@')

    def test_checkSameHusbWife(self):
        self.assertTrue(checkSameHusbWife(self.fam2))
        self.assertFalse(checkSameHusbWife(self.fam1))
        
    def test_checkDeathBeforeBirth(self):
        self.indi.addBirt('9 MAY 1978')
        self.indi.addDeat('9 MAY 1913')
        self.assertTrue(checkDeathBeforeBirth(self.indi))
        
        self.indi.addDeat('9 MAY 1978')
        self.assertFalse(checkDeathBeforeBirth(self.indi))     

        self.indi.addDeat('12 APR 2013')
        self.assertFalse(checkDeathBeforeBirth(self.indi))    
        
        self.indi.addDeat(None)
        self.assertFalse(checkDeathBeforeBirth(self.indi))    
        

if __name__ == '__main__':
    unittest.main()