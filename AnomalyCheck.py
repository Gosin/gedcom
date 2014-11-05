from datetime import datetime


class Anomalies(object):
    def __init__(self):
        self.messages = dict()
        self.messages["checkSameHusbWife"] = "Error: Husband and Wife are same person in family."
        self.messages["checkDeathBeforeBirth"] = "Error: Date of Death is before Date of Birth."
        self.messages["checkMarryDead"] = "Error: Date of marriage is after Date of spouse's death."
        self.messages["checkChildBeforeParents"] = "Error: Children born before parents."
        self.messages["checkWifeIsMale"] = "Anomaly: Wife is male."
        self.messages["checkHusbandIsFemale"] = "Anomaly: Husband is female."

    def getMessage(self, messageId):
        return self.messages[messageId]


def checkSameHusbWife(fam):
    return fam.getHusb() == fam.getWife()

def checkDeathBeforeBirth(individual):
    date_format = "%d %b %Y"
    if individual.getBirt() and individual.getDeat(): 
        return datetime.strptime(individual.getDeat(), date_format) < datetime.strptime(individual.getBirt(), date_format)

def getDeathFromID(ID, individuals):
    for indi in individuals:
        if individuals[indi].getDeat() and individuals[indi].getID() == ID:
            return individuals[indi].getDeat()
    return None

def checkMarryDead(fam, individuals):
    a = False
    b = False
    date_format = "%d %b %Y"
    marry_date = datetime.strptime(fam.getMarr(), date_format)
    if getDeathFromID(fam.getHusb(), individuals):
        husb_death = datetime.strptime(getDeathFromID(fam.getHusb(), individuals), date_format)
        a = husb_death < marry_date

    if getDeathFromID(fam.getWife(), individuals):
        wife_death = datetime.strptime(getDeathFromID(fam.getWife(), individuals), date_format)
        b = wife_death < marry_date

    return (a or b)

def getBirhtFromID(ID, individuals):
    for indi in individuals:
        if individuals[indi].getBirt() and individuals[indi].getID() == ID:
            return individuals[indi].getBirt()
    return None

def checkChildBeforeParents(fam, individuals):
    date_format = "%d %b %Y"
    father = datetime.strptime(getBirhtFromID(fam.getHusb(), individuals), date_format)
    mother = datetime.strptime(getBirhtFromID(fam.getWife(), individuals), date_format)
    anomaly_count = 0
    if fam.getChil():
        for child in fam.getChil():
            birth_of_child = datetime.strptime(getBirhtFromID(child, individuals), date_format)
            if birth_of_child < father or birth_of_child < mother:
                anomaly_count += 1
    if anomaly_count > 0:
        return True
    else:
        return False


def checkWifeIsMale(fam, individuals):
    if fam.getWife():
        for indi in individuals:
            if individuals[indi].getID() == fam.getWife():
                return individuals[indi].getSex()  == "M"
    else:
        return False

def checkHusbandIsFemale(fam, individuals):
    if fam.getHusb():
        for indi in individuals:
            if individuals[indi].getID() == fam.getHusb():
                return individuals[indi].getSex()  == "F"
    else:
        return False
    
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
    return anomalies