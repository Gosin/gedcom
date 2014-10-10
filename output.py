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
