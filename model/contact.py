from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middlename=None, lastname=None, nicknam=None, title=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None,
                 email=None, email2=None, email3=None, secondaryphone=None, id=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None):
        self.first_name = first_name
        self.middlename = middlename
        self.lastname = lastname
        self.nicknam = nicknam
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id

    def __repr__(self):
        return "%s : %s, %s" % (self.id, self.lastname, self.first_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               and (self.first_name is None or other.first_name is None or self.first_name == other.first_name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
