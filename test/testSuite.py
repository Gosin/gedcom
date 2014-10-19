import unittest
from gedcomTest import GedcomTest
from individualTest import IndividualTest
from familyTest import FamilyTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(GedcomTest())
    suite.addTest(IndividualTest())
    suite.addTest(FamilyTest())
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner.run(suite())
