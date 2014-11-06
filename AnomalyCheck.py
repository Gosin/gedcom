from datetime import datetime
from datetime import timedelta


date_format = "%d %b %Y"

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

    def getMessage(self, messageId):
        return self.messages[messageId]


def checkSameHusbWife(fam):
    return fam.getHusb() == fam.getWife()

def checkDeathBeforeBirth(individual):
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
    marry_date = datetime.strptime(fam.getMarr(), date_format)
    if getDeathFromID(fam.getHusb(), individuals):
        husb_death = datetime.strptime(getDeathFromID(fam.getHusb(), individuals), date_format)
        a = husb_death < marry_date

    if getDeathFromID(fam.getWife(), individuals):
        wife_death = datetime.strptime(getDeathFromID(fam.getWife(), individuals), date_format)
        b = wife_death < marry_date

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
    father = datetime.strptime(getBirthFromID(fam.getHusb(), individuals), date_format)
    mother = datetime.strptime(getBirthFromID(fam.getWife(), individuals), date_format)
    anomaly_count = 0
    if fam.getChil():
        for child in fam.getChil():
            birth_of_child = datetime.strptime(getBirthFromID(child, individuals), date_format)
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

def marriedBeforeBirth(fam, individuals):
    marry_date = datetime.strptime(fam.getMarr(), date_format)
    if marry_date < datetime.strptime(getBirthFromID(fam.getHusb(), individuals), date_format):
        return True
    elif marry_date < datetime.strptime(getBirthFromID(fam.getWife(), individuals), date_format):
        return True
    else:
        return False
    
def marriedTooYoung(fam, individuals):
    MARRYING_AGE = 5113
    marry_date = datetime.strptime(fam.getMarr(), date_format)
    if marry_date - datetime.strptime(getBirthFromID(fam.getHusb(), individuals), date_format) < timedelta(days=MARRYING_AGE):
        return True
    elif  marry_date - datetime.strptime(getBirthFromID(fam.getWife(), individuals), date_format) < timedelta(days=MARRYING_AGE):
        return True
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
        if marriedBeforeBirth(families.get(fam), individuals):
            anomalies.append(("marriedBeforeBirth", families.get(fam)))
        if marriedTooYoung(families.get(fam), individuals):
            anomalies.append(("marriedTooYoung", families.get(fam)))
    return anomalies