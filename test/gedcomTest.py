import unittest
from Individual import Individual
from Family import Family
from AnomalyCheck import checkSameHusbWife



class GedcomTest(unittest.TestCase):

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

    def test_getID(self):
        ID = '@I2@'
        self.assertEqual(self.indi.getID(), ID)

    def test_getName(self):
        NAME = 'John Rivas'
        self.assertEqual(self.indi.getName(), NAME)

    def test_getSex(self):
        SEX = 'M'
        self.assertEqual(self.indi.getSex(), SEX)

    def test_getBirt(self):
        BIRT = '9 MAY 1978'
        self.assertEqual(self.indi.getBirt(), BIRT)

    def test_getDeat(self):
        DEAT = '12 APR 2013'
        self.assertEqual(self.indi.getDeat(), DEAT)

    def test_getFams(self):
        FAMS = '@F2@'
        self.assertEqual(self.indi.getFams(), FAMS)

    def test_getFamc(self):
        FAMC = '@F1@'
        self.assertEqual(self.indi.getFamc(), FAMC)

    def test_getFamID(self):
        FAMID = '@F2@'
        self.assertEqual(self.fam1.getFamID(), FAMID)

    def test_getHusb(self):
        HUSB = "@I1@"
        self.assertEqual(self.fam1.getHusb(), HUSB)

    def test_getWife(self):
        WIFE = "@I2@"
        self.assertEqual(self.fam1.getWife(), WIFE)

    def test_getChil(self):
        CHIL = ['@I4@', '@I5@']
        self.assertEqual(self.fam1.getChil(), CHIL)

    def test_getMarr(self):
        MARR = '5 OCT 1999'
        self.assertEqual(self.fam1.getMarr(), MARR)

    def test_getDiv(self):
        DIV = '12 JUN 2012'
        self.assertEqual(self.fam1.getDiv(), DIV)

    def test_checkSameHusbWife(self):
        self.assertTrue(checkSameHusbWife(self.fam2))




if __name__ == '__main__':
    unittest.main()