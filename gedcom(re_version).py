import sys
import time
import re

individuals =[]
families = []
VALID_TAGS = ["INDI", "NAME", "SEX", "BIRT", "DEAT",\
              "FAMC", "FAMS", "FAM", "MARR", "HUSB",\
              "WIFE", "CHIL", "DIV", "DATE", "TRLR",\
              "NOTE"]

# extract 3 parts each line
extract_re = '([0-9]*) (@?\w+@?)\s*([^\n\r]*)'

def extractInfo(input_file):
	indi_tag = False
	prev_tag = ''
	person = dict()
	family = dict()

	for line in input_file:
		if re.match(extract_re, line):
			parts = re.match(extract_re, line).groups()
			part1 = parts[0]
			part2 = parts[1]
			part3 = parts[2]

			if part1 == '0':
				if part3 == "INDI":
					indi_tag = True
					if person:
						individuals.append(person)
						person = dict()
						person['ID'] = part2 
				elif part3 == "FAM":
					indi_tag = False
					if family:
						families.append(family)
						family = dict()
						family['ID'] = part2
			elif part1 == '1':
				if (part2 == "BIRT" or part2 == "DEAT" or 
					part2 == "DIV" or part2 == "MARR"):
					prev_tag = part2
				elif indi_tag and part2 in VALID_TAGS:
					person[part2] = part3
				elif not indi_tag and part2 in VALID_TAGS:
					family[part2] = part3
			elif part1 == '2' and part2 == "DATE":
				if indi_tag:
					person[prev_tag] = part3
					prev_tag = ''
				else:
					family[prev_tag] = part3
					prev_tag = ''
			else:
				print "Unkown Line."
		
		else:
			print "Match Failed."


def checkDeathBeforeBirth(indviduals):
    for indi in individuals:
        if 'DEAT' in individual:
            birt = time.strptime(individual['BIRT'], "%d %b %Y")
            deat = time.strptime(individual['DEAT'], "%d %b %Y")
            if birt > deat:
                print "Date Error: dead before birth. Occured at",
                print individual['INDI'] + " Which is " + individual['NAME']




def main(arg1):
	input_file = open(arg1, 'r')
	extractInfo(input_file)
	input_file.close()


if __name__ == '__main__':
	main(sys.argv[1])