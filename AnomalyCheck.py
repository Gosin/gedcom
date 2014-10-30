from datetime import datetime
from family import Family
from individual import Individual


class Anomalies(object):
    def __init__(self):
        self.messages = dict()
        self.messages["checkSameHusbWife"] = "Error: Husband and Wife are same person in family."
        self.messages["checkDeathBeforeBirth"] = "Error: Date of Death is before Date of Birth."
        self.messages["checkMarryDead"] = "Error: Date of marriage is after Date of spouse's death."

    def getMessage(self, messageId):
        return self.messages[messageId]


def checkSameHusbWife(fam):
    return fam.getHusb() == fam.getWife()

def checkDeathBeforeBirth(individual):
    date_format = "%d %b %Y"
    if individual.getBirt() and individual.getDeat(): 
        return datetime.strptime(individual.getDeat(), date_format) < datetime.strptime(individual.getBirt(), date_format)

def getDeathFromID(id, individuals):
    for indi in individuals:
        if individuals[indi].getDeat() and individuals[indi].getID() == id:
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
    return anomalies