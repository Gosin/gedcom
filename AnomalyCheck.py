def checkSameHusbWife(fam):

	husb = fam.getHusb()
	wife = fam.getWife()
	if husb == wife:
		print "Husband and Wife are same person in family: ",
		print fam.getFamID()
		return True
	else:
		return False
