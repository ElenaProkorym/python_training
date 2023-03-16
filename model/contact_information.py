from sys import maxsize
class ContactInfo:
    def __init__(self, id = None, firstname = None, lastname = None, address = None,
                 homephone = None, mobilephone = None, workphone = None, faxphone = None, secondaryphone = None,
                 company = None, email = None, email2 = None, email3 = None, secondaryaddress = None, all_phones_from_home_page = None,
                 all_email_address_from_home_page = None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.homephone = homephone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.faxphone = faxphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_address_from_home_page = all_email_address_from_home_page
        #self.all_address_from_home_page = all_address_from_home_page
        self.secondaryaddress = secondaryaddress

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