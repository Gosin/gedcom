def outputIndiSummary(individuals):

	total_indis = len(individuals)
	print "There are %s individuals in this family." % total_indis
	for indi in individuals:
		indi_id = individuals[indi].getID()
		indi_name = individuals[indi].getName()
		print indi_id + ": " + indi_name
