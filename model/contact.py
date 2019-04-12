from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middlename=None, lastname=None, nicknam=None, title=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None,
                 email=None, email2=None, email3=None, secondaryphone=None, id=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None, all_phones_from_db=None, all_emails_from_db=None):
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
        self.all_phones_from_db = all_phones_from_db
        self.all_emails_from_db = all_emails_from_db

    def __repr__(self):
        return "%s : %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id, self.lastname, self.first_name, self.address, self.home, self.mobile, self.work, self.fax,
            self.email, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.first_name is None or other.first_name is None or self.first_name == other.first_name) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) and (
                       self.address is None or other.address is None or self.address == other.address) and (
                       self.home is None or other.home is None or self.home == other.home) and (
                       self.mobile is None or other.mobile is None or self.mobile == other.mobile) and (
                       self.work is None or other.work is None or self.work == other.work) and (
                       self.fax is None or other.fax is None or self.fax == other.fax) and (
                       self.email is None or other.email is None or self.email == other.email) and (
                       self.email2 is None or other.email2 is None or self.email2 == other.email2) and (
                       self.email3 is None or other.email3 is None or self.email3 == other.email3)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
