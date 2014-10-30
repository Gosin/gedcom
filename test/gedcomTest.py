import unittest
from family import Family
from individual import Individual
from AnomalyCheck import checkSameHusbWife
from AnomalyCheck import checkDeathBeforeBirth
from AnomalyCheck import checkMarryDead
from AnomalyCheck import checkChildBeforeParents


class GedcomTest(unittest.TestCase):
    def setUp(self):
        self.indi1 = Individual()
        self.indi1.addID('@I1@')
        self.indi1.addName('John Rivas')
        self.indi1.addSex('M')
        self.indi1.addBirt('9 MAY 1978')
        self.indi1.addDeat('12 APR 2013')
        self.indi2 = Individual()
        self.indi2.addID('@I2@')
        self.indi2.addName('Mary Rivas')
        self.indi2.addSex('F')
        self.indi2.addBirt('21 APR 1980')
        self.indi2.addDeat('12 SEP 1990')
        self.indi3 = Individual()
        self.indi3.addID('@I3@')
        self.indi3.addName('Mary Rivas')
        self.indi3.addSex('F')
        self.indi3.addBirt('21 APR 1980')
        self.indi3.addDeat('12 SEP 2014')
        self.indi4 = Individual()
        self.indi4.addID('@I4@')
        self.indi4.addName('Mike Rivas')
        self.indi4.addSex('M')
        self.indi4.addBirt('21 APR 1976')
        self.indi5 = Individual()
        self.indi5.addID('@I5@')
        self.indi5.addName('Mike Rivas')
        self.indi5.addSex('M')
        self.indi5.addBirt('21 APR 2012')

        self.individuals = dict()
        self.individuals['1'] = self.indi1
        self.individuals['2'] = self.indi2
        self.individuals['3'] = self.indi3
        self.individuals['4'] = self.indi4
        self.individuals['5'] = self.indi5

        
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
        self.fam3 = Family()
        self.fam3.addFamID('@F3@')
        self.fam3.addHusb('@I1@')
        self.fam3.addWife('@I2@')
        self.fam3.addChil('@I4@')
        self.fam3.addChil('@I5@')
        self.fam3.addMarr('5 OCT 1999')
        self.fam3.addDiv('12 JUN 2012')
        self.fam4 = Family()
        self.fam4.addFamID('@F4@')
        self.fam4.addHusb('@I1@')
        self.fam4.addWife('@I3@')
        self.fam4.addChil('@I4@')
        self.fam4.addMarr('5 OCT 1999')
        self.fam4.addDiv('12 JUN 2012')
        self.fam5 = Family()
        self.fam5.addFamID('@F5@')
        self.fam5.addHusb('@I1@')
        self.fam5.addWife('@I3@')
        self.fam5.addChil('@I5@')
        self.fam5.addMarr('5 OCT 1999')
        self.fam5.addDiv('12 JUN 2012')

    def test_checkSameHusbWife(self):
        self.assertTrue(checkSameHusbWife(self.fam2))
        self.assertFalse(checkSameHusbWife(self.fam1))
        
    def test_checkDeathBeforeBirth(self):
        self.indi1.addBirt('9 MAY 1978')
        self.indi1.addDeat('9 MAY 1913')
        self.assertTrue(checkDeathBeforeBirth(self.indi1))
        
        self.indi1.addDeat('9 MAY 1978')
        self.assertFalse(checkDeathBeforeBirth(self.indi1))     

        self.indi1.addDeat('12 APR 2013')
        self.assertFalse(checkDeathBeforeBirth(self.indi1))    
        
        self.indi1.addDeat(None)
        self.assertFalse(checkDeathBeforeBirth(self.indi1))

    def test_checkMarryDead(self):
        self.assertTrue(checkMarryDead(self.fam3, self.individuals))
        self.assertFalse(checkMarryDead(self.fam4, self.individuals))

    def test_checkChildBeforeParents(self):
        self.assertTrue(checkChildBeforeParents(self.fam4, self.individuals))
        self.assertFalse(checkChildBeforeParents(self.fam5, self.individuals))

        

if __name__ == '__main__':
    unittest.main()