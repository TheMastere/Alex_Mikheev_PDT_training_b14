from sys import maxsize


class New_contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, fax=None, email1=None, email2=None,
                 email3=None,
                 all_email=None, all_phones_from_home_page=None, email=None, address2=None, secondary_phone=None,
                 notes=None,
                 id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.all_email = all_email
        self.address = address
        self.fax = fax
        self.email = email
        self.address2 = address2
        self.secondary_phone = secondary_phone
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (
        self.id, self.lastname, self.firstname, self.middlename,
        self.nickname, self.title, self.address, self.homephone, self.address2,
        self.workphone, self.mobilephone, self.secondary_phone,
        self.email, self.company, self.fax, self.notes)

    def __eq__(self, other):
        return self.id is None or other.id is None or self.id == other.id and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
