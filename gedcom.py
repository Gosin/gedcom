'''

SSW555 Stevens IT Team Two

'''
import sys

individuals= []
families = []

def gatherInfo(input_file):
    ID_TAGS = ['INDI', 'FAM']
    person = dict()
    family = dict()
    
    for line in input_file:
        if validateTag(getLevel(line), getTag(line)):
            if getTag(line) in ID_TAGS:
                if person:
                    individuals.append(person)
                    person = dict()
                if family:
                    families.append(family)
                    family = dict()
                
            if getTag(line) == "INDI":
                indi_tag = True
            elif getTag(line) == "FAM":
                indi_tag = False
                
            if indi_tag:
                if getTag(line) == "BIRT" or getTag(line) == "DEAT":
                    prev_tag = getTag(line) 
                elif getTag(line) == "DATE":    
                    person[prev_tag] = getArguments(line)
                else:
                    person[getTag(line)] = getArguments(line)
            else:
                if getTag(line) == "DIV" or getTag(line) == "MARR":
                    prev_tag = getTag(line) 
                elif getTag(line) == "DATE":    
                    person[prev_tag] = getArguments(line)
                else:
                    family[getTag(line)] = getArguments(line)
                
    printIndividualsNames(individuals)
    printFamiliesParents(families, individuals)

   
def printIndividualsNames(individuals):
    individuals.sort(key=lambda k:k['INDI'])
    for indi in individuals:
        print getIndiName(indi)
        
def printFamiliesParents(families, individuals):
    families.sort(key=lambda k:k['FAM'])
    for fam in families:
        print getIndiName(getIndividual(individuals,getHusbandId(fam))), getIndiName(getIndividual(individuals,getWifeId(fam)))
        
    
def printLines(input_file):
    for line in input_file:
        if validateTag(getLevel(line), getTag(line)):
            print line,
        
def getLevel(line):
    LEVEL_POS = 0
    return line.split()[LEVEL_POS]

    
def getTag(line):
    TAG_POS = 1
    if int(getLevel(line)):
        return line.split()[TAG_POS]
    else:
        return getZeroTag(line)

def getArguments(line):
    ARG_POS = 2
    ID_POS = 1
    if getLevel(line) == '0':
        return line.split()[ID_POS]
    
    if len(line.split()) > ARG_POS:
        args = line.split()[ARG_POS:]
        return ' '.join(args)

     
def getUniqueId(line):
    ID_POS = 1
    if int(getLevel(line)) == 0:
        return line.split()[ID_POS]

def getZeroTag(line): 
    ID_TAGS = ['INDI', 'FAM']
    ID_POS = 2
    TAG_POS = 1
    parts = line.split()
    
    if int(getLevel(line)):
        return None
    
    if len(parts) > ID_POS:
        if parts[ID_POS] in ID_TAGS:
            return parts[ID_POS]
    else:
        return parts[TAG_POS]
   
def validateTag(level, tag): 
    VALID_TAGS = [['0', 'INDI'], 
                  ['1', 'NAME'],
                  ['1', 'SEX'],
                  ['1', 'BIRT'],
                  ['1', 'DEAT'],
                  ['1', 'FAMC'],
                  ['1', 'FAMS'],
                  ['0', 'FAM'],
                  ['1', 'MARR'],
                  ['1', 'HUSB'],
                  ['1', 'WIFE'],
                  ['1', 'CHIL'],
                  ['1', 'DIV'],
                  ['2', 'DATE'],
                  ['0', 'TRLR'],
                  ['0', 'NOTE']] 
    tag_with_level = [level, tag] 
    return tag_with_level in VALID_TAGS

def getIndividual(individuals, uniqueId):
    for indi in individuals:
        if indi['INDI'] == uniqueId:
            return indi

def getIndiName(individual):
    return individual['NAME']


    
def getHusbandId(family):
    return family['HUSB']

def getWifeId(family):
    return family['WIFE']
     
def main(arg1):
    input_file = open(arg1, 'r')
    gatherInfo(input_file)
    input_file.close()
    
    
if __name__ == '__main__':
    main(sys.argv[1])