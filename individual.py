class Individual(object):

    def __init__(self):
        self.ID = ''
        self.name = ''
        self.sex = ''
        self.birt = ''
        self.deat = ''
        self.fam_id = ''


    def add_ID(self, ID):
        if re.match('@\w+@', ID):
            self.ID = ID
        else:
            print "Invalid ID."
    
    def add_name(self, name):
        self.name = name

    def add_sex(self, sex):
        if sex == 'M' or sex == 'F':
            self.sex = sex
        else:
            print "Invalid sex value."

    def add_birt(self, birt):
        self.birt = birt

    def add_deat(self, deat):
        self.deat = deat

    def add_fam_id(self, fam_id):
        if re.match('@\w+@', fam_id):
            self.fam_id = fam_id
        else:
            print "Invalid Family ID."

    def get_ID(self):
        if self.ID:
            return self.ID
        else:
            print "ID doesn't exits."

    def get_name(self):
        return self.name

    def get_birt(self):
        return self.birt

    def get_deat(self):
        if self.deat:
            return self.deat
        else:
            print "No death date available."

    def get_fam_id(self):
        return self.fam_id