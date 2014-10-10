def outputIndiSummary(individuals):

	total_indis = len(individuals)
	print "There are %s individuals in this House." % total_indis
	print "Here is the list: "
	for indi in individuals:
		indi_id = individuals[indi].getID()
		indi_name = individuals[indi].getName()
		print indi_id + ": " + indi_name

def outputFamSummary(families):

	total_fams = len(families)
	print "There are %s families in this House." % total_fams
	print "Here is the list: ",
	for fam in families:
		print "\n"
		fam_id = families[fam].getFamID()
		fam_husb = families[fam].getHusb()
		fam_wife = families[fam].getWife()
		fam_chil = families[fam].getChil()
		print "Family ID: " + fam_id
		print "Husband: " + fam_husb + ", Wife: " + fam_wife
		if fam_chil:
			print "Children: ",
			for child in fam_chil:
				print child + " ",
		else:
			print "There're no children in this family.",