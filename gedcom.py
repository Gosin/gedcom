'''

SSW555 Stevens IT Team Two

'''
import sys
import time
import re
from Individual import Individual
from Family import Family

individuals = dict()
families = dict()

VALID_TAGS = ["INDI", "NAME", "SEX", "BIRT", "DEAT",\
              "FAMC", "FAMS", "FAM", "MARR", "HUSB",\
              "WIFE", "CHIL", "DIV", "DATE", "TRLR",\
              "NOTE"]
extract_re = '([0-9]*) (@?\w+@?)\s*([^\n\r]*)'

def gatherInfo(input_file):

    # tag category: 0 for indi, 1 for fam, 2 for others
    tagCat = 2

    prevTag = ''
    tempID = ''
    tempFamID = ''

    for line in input_file:
        if re.match(extract_re, line):
            parts = re.match(extract_re, line).groups()
            part1 = parts[0]
            part2 = parts[1]
            part3 = parts[2]

            if part1 == '0':
                if part3 == "INDI":
                    tagCat = 0
                    indi_tag = True
                    tempID = part2
                    individuals[tempID] = Individual()
                    individuals[tempID].addID(part2)
                elif part3 == 'FAM':
                    tagCat = 1
                    indi_tag = False
                    tempFamID = part2
                    families[tempFamID] = Family()
                    families[tempFamID].addFamID(part2)
                else:
                    tagCat = 2

            elif part1 == '1':
                if tagCat == 0:
                    if part2 == "BIRT" or part2 == "DEAT":
                        prevTag = part2
                    elif part2 == 'NAME':
                        individuals[tempID].addName(part3)
                    elif part2 == 'SEX':
                        individuals[tempID].addSex(part3)
                    elif part2 == 'FAMC':
                        individuals[tempID].addFamc(part3)
                    elif part2 == 'FAMS':
                        individuals[tempID].addFams(part3)
                    else:
                        pass

                elif tagCat == 1:
                    if part2 == "MARR" or part2 == "DIV":
                        prevTag = part2
                    elif part2 == 'HUSB':
                        families[tempFamID].addHusb(part3)
                    elif part2 == 'WIFE':
                        families[tempFamID].addWife(part3)
                    elif part2 == "CHIL":
                        families[tempFamID].addChil(part3)
                    else:
                        pass

                elif tagCat == 2:
                    pass

            elif part1 == '2' and part2 == 'DATE':
                if tagCat == 0:
                    if prevTag == 'BIRT':
                        individuals[tempID].addBirt(part3)
                    elif prevTag == 'DEAT':
                        individuals[tempID].addDeat(part3)
                    else:
                        pass

                elif tagCat == 1:
                    if prevTag == 'MARR':
                        families[tempFamID].addMarr(part3)
                    elif prevTag == 'DIV':
                        families[tempFamID].addDiv(part3)
                    else:
                        pass

                else:
                    pass


def main(arg1):
    input_file = open(arg1, 'r')
    gatherInfo(input_file)
    for indi in individuals:
        a = individuals[indi].getName()
        print a
    input_file.close()

if __name__ == '__main__':
    main(sys.argv[1])