class Family(object):

    def __init__(self):
        self.fam_id = ''
        self.husb = ''
        self.wife = ''
        self.marr = ''
        self.chil = []

    def add_fam_id(self, fam_id):
        if re.match('@\w+@', fam_id):
            self.fam_id = fam_id
        else:
            print "Invalid Family ID."

    def add_husb(self, husb):
        self.husb = husb

    def add_wife(self, wife):
        self.wife = wife

    def add_marr(self, marr):
        self.marr = marr

    def add_chil(self, chil):
        self.chil.append(chil)

    def get_husb(self):
        return self.husb

    def get_wife(self):
        return self.wife

    def get_marr(self):
        return self.marr

    def get_child(self):
        return self.chil