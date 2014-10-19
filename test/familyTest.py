import unittest
from family import Family

class FamilyTest(unittest.TestCase):
    def setUp(self):
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

    """ Test setters """    
    
    def test_addFamID(self):
        fam = Family()
        value = '@A1@'
        fam.addFamID(value)
        self.assertEqual(fam.getFamID(), value)

    def test_addHusb(self):
        fam = Family()
        value = '@A1@'
        fam.addHusb(value)
        self.assertEqual(fam.getHusb(), value)   
    
    def test_addWife(self):
        fam = Family()
        value = '@A1@'
        fam.addWife(value)
        self.assertEqual(fam.getWife(), value)    
    
    def test_addChil(self):
        fam = Family()
        value = '@A1@'
        fam.addChil(value)
        self.assertEqual(fam.getChil()[0], value)  
    

        
    """ Test getters """   

    def test_getFamID(self):
        FAMID = '@F2@'
        self.assertEqual(self.fam1.getFamID(), FAMID)
        
        fam = Family()
        self.assertEqual(fam.getFamID(), None)

    def test_getHusb(self):
        HUSB = "@I1@"
        self.assertEqual(self.fam1.getHusb(), HUSB)
        
        fam = Family()
        self.assertEqual(fam.getHusb(), None)
        
    def test_getWife(self):
        WIFE = "@I2@"
        self.assertEqual(self.fam1.getWife(), WIFE)
        
        fam = Family()
        self.assertEqual(fam.getWife(), None)
        
    def test_getChil(self):
        CHIL = ['@I4@', '@I5@']
        self.assertEqual(self.fam1.getChil(), CHIL)
        
        fam = Family()
        self.assertEqual(fam.getChil(), [])
        
    def test_getMarr(self):
        MARR = '5 OCT 1999'
        self.assertEqual(self.fam1.getMarr(), MARR)
        
        fam = Family()
        self.assertEqual(fam.getMarr(), None)
        
    def test_getDiv(self):
        DIV = '12 JUN 2012'
        self.assertEqual(self.fam1.getDiv(), DIV)
        
        fam = Family()
        self.assertEqual(fam.getDiv(), None)
        
if __name__ == '__main__':
    unittest.main()