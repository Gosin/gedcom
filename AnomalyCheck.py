from datetime import datetime
from family import Family
from individual import Individual


class Anomalies(object):
    def __init__(self):
        self.messages = dict()
        self.messages["checkSameHusbWife"] = "Error: Husband and Wife are same person in family."
        self.messages["checkDeathBeforeBirth"] = "Error: Date of Death is before Date of Birth."

    def getMessage(self, messageId):
        return self.messages[messageId]


def checkSameHusbWife(fam):
    return fam.getHusb() == fam.getWife()

def checkDeathBeforeBirth(individual):
    date_format = "%d %b %Y"
    if individual.getBirt() and individual.getDeat(): 
        return datetime.strptime(individual.getDeat(), date_format) < datetime.strptime(individual.getBirt(), date_format)


def checkAnomalies(people):
    anomalies = []
    for p in people:
        if isinstance(people.get(p), Individual):
            if checkDeathBeforeBirth(people.get(p)):
                anomalies.append(("checkDeathBeforeBirth", people.get(p)))
                
        if isinstance(people.get(p), Family):
            if checkSameHusbWife(people.get(p)):
                anomalies.append(("checkSameHusbWife", people.get(p)))
    return anomalies