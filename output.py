from AnomalyCheck import Anomalies
from family import Family
from individual import Individual

def outputIndiSummary(individuals):

	print "There are %s individuals in this House." % len(individuals)
	print "Here is the list: "
	for indi in individuals:
		indi_id = individuals[indi].getID()
		indi_name = individuals[indi].getName()
		print indi_id + ": " + indi_name

def outputFamSummary(families, individuals):

	print "There are %s families in this House." % len(families)
	print "Here is the list: ",
	for fam in families:
		print "\n"
		fam_id = families[fam].getFamID()
		fam_husb = families[fam].getHusb()
		fam_wife = families[fam].getWife()
		fam_chil = families[fam].getChil()
		print "Family ID: " + fam_id
		if fam_husb:
			print "Husband: " + fam_husb + " : " +  getNameFromID(individuals, fam_husb) 
		if fam_wife:
			print	"Wife: " + fam_wife + " : "  + getNameFromID(individuals, fam_wife)
		if fam_chil:
			print "Children: ",
			for child in fam_chil:
				print child + " " + getNameFromID(individuals, child),
		else:
			print "There are no children in this family.",
			
def outputAnomalies(anomalies):
	for a in anomalies:
		print Anomalies().getMessage(a[0]), 
		if isinstance(a[1], Family):
			print a[1].getFamID()
		
		if isinstance(a[1], Individual):
			print a[1].getID() + ": " + a[1].getName()

def getNameFromID(individuals,ID):
	for i in individuals:
		if individuals[i].getID() == ID:
			return individuals[i].getName()
	
	return None

	
	