import unittest
from gedcomTest import GedcomTest
from individualTest import IndividualTest
from familyTest import FamilyTest


def suite():
    suite = unittest.TestSuite()
    for method in dir(GedcomTest):
        if method.startswith("test"):
            suite.addTest(GedcomTest(method))
    for method in dir(IndividualTest):
        if method.startswith("test"):
            suite.addTest(IndividualTest(method))
    for method in dir(FamilyTest):
        if method.startswith("test"):
            suite.addTest(FamilyTest(method))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
