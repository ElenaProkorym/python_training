from sys import maxsize
class ContactInfo:
    def __init__(self,address = None, company = None, firstname = None, home = None, lastname = None, email = None, id = None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.home = home
        self.email = email
        self.id = id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
            and (self.firstname is None or other.firstname is None or self.firstname == other.firstname)\
            and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def __repr__(self):
        return "%s : %s : %s" % (self.id, self.firstname, self.lastname)