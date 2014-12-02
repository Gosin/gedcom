from datetime import datetime
from datetime import timedelta



class Anomalies(object):
    def __init__(self):
        self.messages = dict()
        self.messages["checkSameHusbWife"] = "Error: Husband and Wife are same person in family."
        self.messages["checkDeathBeforeBirth"] = "Error: Date of Death is before Date of Birth."
        self.messages["checkMarryDead"] = "Error: Date of marriage is after Date of spouse's death."
        self.messages["checkChildBeforeParents"] = "Error: Children born before parents."
        self.messages["checkWifeIsMale"] = "Anomaly: Wife is male."
        self.messages["checkHusbandIsFemale"] = "Anomaly: Husband is female."
        self.messages["marriedBeforeBirth"] = "Error: Married before birth."
        self.messages["marriedTooYoung"] = "Anomaly: Married at young age."
        self.messages["divorceBeforeMarriage"] = "Anomaly: Divorce before marriage."
        self.messages["tooManyChildren"] = "Anomaly: Large number of children."
        self.messages["tooOldParent"] = "Anomaly: Child born to older parent."
        self.messages["marriedMoreThanOnePerson"] = "Anomaly: Multiple marriages."
        

    def getMessage(self, messageId):
        return self.messages[messageId]


def getDate(gedDate):
    date_format = "%d %b %Y"
    return  datetime.strptime(gedDate, date_format)

def checkSameHusbWife(fam):
    return fam.getHusb() == fam.getWife()

def checkDeathBeforeBirth(individual):
    if individual.getBirt() and individual.getDeat(): 
        return getDate(individual.getDeat()) < getDate(individual.getBirt())

def getDeathFromID(ID, individuals):
    for indi in individuals:
        if individuals[indi].getDeat() and individuals[indi].getID() == ID:
            return individuals[indi].getDeat()
    return None

def checkMarryDead(fam, individuals):
    a = False
    b = False
    if getDeathFromID(fam.getHusb(), individuals):
        husb_death = getDate(getDeathFromID(fam.getHusb(), individuals))
        a = husb_death < getDate(fam.getMarr())

    if getDeathFromID(fam.getWife(), individuals):
        wife_death = getDate(getDeathFromID(fam.getWife(), individuals))
        b = wife_death < getDate(fam.getMarr())

    return (a or b)

def getBirthFromID(ID, individuals):
    for indi in individuals:
        if individuals[indi].getBirt() and individuals[indi].getID() == ID:
            return individuals[indi].getBirt()
    return None

def getSexFromID(ID, individuals):
    for indi in individuals:
        if individuals[indi].getSex() and individuals[indi].getID() == ID:
            return individuals[indi].getSex()
    return None


def checkChildBeforeParents(fam, individuals):
    father = getDate(getBirthFromID(fam.getHusb(), individuals))
    mother = getDate(getBirthFromID(fam.getWife(), individuals))
    anomaly_count = 0
    if fam.getChil():
        for child in fam.getChil():
            birth_of_child = getDate(getBirthFromID(child, individuals))
            if birth_of_child < father or birth_of_child < mother:
                anomaly_count += 1
    if anomaly_count > 0:
        return True
    else:
        return False


def checkWifeIsMale(fam, individuals):
    return getSexFromID(fam.getWife(), individuals)  == "M"

def checkHusbandIsFemale(fam, individuals):
    return getSexFromID(fam.getHusb(), individuals)  == "F"

def deathBeforeMarriage(fam, individuals):
    if  getDeathFromID(fam.getHusb(), individuals) and getDate(getDeathFromID(fam.getHusb(), individuals)) < getDate(fam.getMarr()):
        return True
    elif getDeathFromID(fam.getWife(), individuals) and getDate(getDeathFromID(fam.getWife(), individuals)) < getDate(fam.getMarr()):
        return True
    else:
        return False

def divorceBeforeMarriage(fam, individuals):
    if fam.getDiv() and fam.getMarr():
        return getDate(fam.getDiv()) < getDate(fam.getMarr()) 
    else:
        return False

def marriedBeforeBirth(fam, individuals):
    if getDate(fam.getMarr()) < getDate(getBirthFromID(fam.getHusb(), individuals)):
        return True
    elif getDate(fam.getMarr()) < getDate(getBirthFromID(fam.getWife(), individuals)):
        return True
    else:
        return False
    
def marriedTooYoung(fam, individuals):
    MARRYING_AGE = 5113
    if getDate(fam.getMarr()) - getDate(getBirthFromID(fam.getHusb(), individuals)) >= timedelta(0) and \
        getDate(fam.getMarr()) - getDate(getBirthFromID(fam.getHusb(), individuals))< timedelta(days=MARRYING_AGE):
        return True
    elif  getDate(fam.getMarr()) - getDate(getBirthFromID(fam.getWife(), individuals)) >= timedelta(0) and \
        getDate(fam.getMarr()) - getDate(getBirthFromID(fam.getWife(), individuals)) < timedelta(days=MARRYING_AGE):
        return True
    else:
        return False
    
def tooManyChildren(fam):
    CHILDREN_MAX = 4
    return len(fam.getChil()) > CHILDREN_MAX

def tooOldParent(fam, individuals):
    PARENT_AGE_MAX = 21915
    for child in fam.getChil():
        if getDate(getBirthFromID(child, individuals)) - getDate(getBirthFromID(fam.getHusb(), individuals)) > timedelta(days=PARENT_AGE_MAX):
            return True
        elif getDate(getBirthFromID(child, individuals)) - getDate(getBirthFromID(fam.getWife(), individuals)) > timedelta(days=PARENT_AGE_MAX):
            return True
        else:
            return False

def marriedMoreThanOnePerson(families):
    married = set()
    multiple = set()
    
    for fam in families:
        if not families[fam].getDiv() and not checkSameHusbWife(families[fam]):
            if families[fam].getHusb():
                if families[fam].getHusb() not in married:
                    married.add(families[fam].getHusb())
                else:
                    multiple.add(families[fam].getHusb())
            if families[fam].getWife():
                if families[fam].getWife() not in married:
                    married.add(families[fam].getWife())
                else:
                    multiple.add(families[fam].getWife())
    return multiple
            
        
def checkAnomalies(individuals, families):
    anomalies = []
    for indi in individuals:
        if checkDeathBeforeBirth(individuals.get(indi)):
            anomalies.append(("checkDeathBeforeBirth", individuals.get(indi)))
    for fam in families:
        if checkSameHusbWife(families.get(fam)):
            anomalies.append(("checkSameHusbWife", families.get(fam)))
        if checkMarryDead(families.get(fam), individuals):
            anomalies.append(("checkMarryDead", families.get(fam)))
        if checkChildBeforeParents(families.get(fam), individuals):
            anomalies.append(("checkChildBeforeParents", families.get(fam)))
        if checkWifeIsMale(families.get(fam), individuals):
            anomalies.append(("checkWifeIsMale", families.get(fam)))
        if checkHusbandIsFemale(families.get(fam), individuals):
            anomalies.append(("checkHusbandIsFemale", families.get(fam)))
        if marriedBeforeBirth(families.get(fam), individuals):
            anomalies.append(("marriedBeforeBirth", families.get(fam)))
        if marriedTooYoung(families.get(fam), individuals):
            anomalies.append(("marriedTooYoung", families.get(fam)))
        if divorceBeforeMarriage(families.get(fam), individuals):
            anomalies.append(("divorceBeforeMarriage", families.get(fam)))
        if tooManyChildren(families.get(fam)):
            anomalies.append(("tooManyChildren", families.get(fam)))
        if tooOldParent(families.get(fam), individuals):
            anomalies.append(("tooOldParent", families.get(fam)))
    multiple_marriages = marriedMoreThanOnePerson(families)
    if multiple_marriages:
        anomalies.append(("marriedMoreThanOnePerson", ', '.join(multiple_marriages)))
    return anomalies
