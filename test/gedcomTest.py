import unittest
from gedcom import getTag
from gedcom import getLevel
from gedcom import getBirthDate
from gedcom import getDeathDate
from gedcom import validateDeathDate


class GedcomTest(unittest.TestCase):

    def setUp(self):
        self.line_indi = "0 @I1@ INDI"
        self.line_name = "2 NAME Papa Bear"
        self.person = dict()
        self.person["BIRT"] = "8 JAN 1936"
        self.person["DEAT"] = "9 JAN 1970"
        
    def test_getLevel(self):
        LEVEL = "0"
        self.assertEqual(getLevel(self.line_indi), LEVEL)
        self.assertNotEqual(getLevel(self.line_name), LEVEL)
        
        LEVEL = "2"
        self.assertEqual(getLevel(self.line_name), LEVEL)
        self.assertNotEqual(getLevel(self.line_indi), LEVEL)
        
    def test_getTag(self):
        TAG = "INDI"
        self.assertEqual(getTag(self.line_indi), TAG)
        self.assertNotEqual(getLevel(self.line_name), TAG)
        
        TAG = "NAME"
        self.assertEqual(getTag(self.line_name), TAG)
        self.assertNotEqual(getLevel(self.line_indi), TAG)
        
    def test_getBirthDate(self):
        DATE = self.person["BIRT"]
        self.assertEqual(getBirthDate(self.person), DATE)
        DATE = self.person["DEAT"]
        self.assertNotEqual(getBirthDate(self.person), DATE)
        
    def test_getDeathDate(self):
        DATE = self.person["DEAT"]
        self.assertEqual(getDeathDate(self.person), DATE)
        self.person["DEAT"] = "1 JAN 1600"
        self.assertNotEqual(getDeathDate(self.person), DATE)
        
    def test_validateDeathDate(self):
        self.assertTrue(validateDeathDate(self.person))
        self.person["DEAT"] = "1 JAN 1600"
        self.assertFalse(validateDeathDate(self.person))
        


if __name__ == '__main__':
    unittest.main()