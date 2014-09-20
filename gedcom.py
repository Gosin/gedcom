'''
Created on Sep 12, 2014

SSW555 P02

@author: Brad Senetza
'''
import sys

def printLines(filename):
    input_file = open(filename, 'r')
    for line in input_file:
        print line,
        print getLevel(line)
        print getTag(line) if validateTag(getLevel(line), getTag(line)) else 'Invalid tag'  
         
    input_file.close()
        
def getLevel(line):
    LEVEL = 0
    return line.split()[LEVEL]

    
def getTag(line):
    TAG_POS = 1
    if int(getLevel(line)):
        return line.split()[TAG_POS]
    else:
        return getZeroTag(line)

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
    
     
def main(arg1):
    filename = arg1
    printLines(filename)
    
    
if __name__ == '__main__':
    main(sys.argv[1])