import unittest
from individual import Individual

class IndividualTest(unittest.TestCase):

    def setUp(self):
        self.indi = Individual()
        self.indi.addID('@I2@')
        self.indi.addName('John Rivas')
        self.indi.addSex('M')
        self.indi.addBirt('9 MAY 1978')
        self.indi.addDeat('12 APR 2013')
        self.indi.addFams('@F2@')
        self.indi.addFamc('@F1@')
        
    """ Test setters """    
    
    def test_addID(self):
        indi = Individual()
        value = '@A1@'
        indi.addID(value)
        self.assertEqual(indi.getID(), value)

    def test_addName(self):
        indi = Individual()
        value = "Gloop"
        indi.addName(value)
        self.assertEqual(indi.getName(), value)      
    
    def test_addSex(self):
        indi = Individual()
        value = "M"
        indi.addSex(value)
        self.assertEqual(indi.getSex(), value)  
        
        value = "F"
        indi.addSex(value)
        self.assertEqual(indi.getSex(), value)      
    
    def test_addBirt(self):
        indi = Individual()
        value = "01 JAN 1900"
        indi.addBirt(value)
        self.assertEqual(indi.getBirt(), value)   
    
    def test_addDeat(self):
        indi = Individual()
        value = "01 JAN 2000"
        indi.addDeat(value)
        self.assertEqual(indi.getDeat(), value)   

    def test_addFams(self):
        indi = Individual()
        value = '@A1@'
        indi.addFams(value)
        self.assertEqual(indi.getFams()[0], value)  

    def test_addFamc(self):
        indi = Individual()
        value = '@A1@'
        indi.addFamc(value)
        self.assertEqual(indi.getFamc()[0], value)  
            
            
    """ Test getters """    
            
    def test_getID(self):
        ID = '@I2@'
        self.assertEqual(self.indi.getID(), ID)
        
        indi = Individual()
        self.assertEqual(indi.getID(), None)

    def test_getName(self):
        NAME = 'John Rivas'
        self.assertEqual(self.indi.getName(), NAME)
        
        indi = Individual()
        self.assertEqual(indi.getName(), None)

    def test_getSex(self):
        SEX = 'M'
        self.assertEqual(self.indi.getSex(), SEX)
        
        indi = Individual()
        self.assertEqual(indi.getSex(), None)

    def test_getBirt(self):
        BIRT = '9 MAY 1978'
        self.assertEqual(self.indi.getBirt(), BIRT)
        
        indi = Individual()
        self.assertEqual(indi.getBirt(), None)
        
    def test_getDeat(self):
        DEAT = '12 APR 2013'
        self.assertEqual(self.indi.getDeat(), DEAT)

        indi = Individual()
        self.assertEqual(indi.getDeat(), None)
        
    def test_getFams(self):
        FAMS = ['@F2@']
        self.assertEqual(self.indi.getFams(), FAMS)
        
        indi = Individual()
        self.assertEqual(indi.getFams(), [])
        
    def test_getFamc(self):
        FAMC = ['@F1@']
        self.assertEqual(self.indi.getFamc(), FAMC)
        
        indi = Individual()
        self.assertEqual(indi.getFamc(), [])
        
        
if __name__ == '__main__':
    unittest.main()