from family import Family
from individual import Individual
class Anomalies(object):
	
	
	def __init__(self):
		self.messages = dict()
		self.messages["checkSameHusbWife"] = "Error: Husband and Wife are same person in family."

	def getMessage(self, messageId):
		return self.messages[messageId]

def checkSameHusbWife(fam):
	return fam.getHusb() == fam.getWife()



def checkAnomalies(people):
	anomalies = []
	for p in people:
		if isinstance(people.get(p), Individual):   
			pass
		if isinstance(people.get(p), Family): 
			if checkSameHusbWife(people.get(p)):
				anomalies.append(("checkSameHusbWife",people.get(p)))
	return anomalies