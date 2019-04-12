import pymysql

from model.contact import Contact
from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))

        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, middlename, lastname, company from addressbook WHERE deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, company) = row
                list.append(Contact(id=str(id), first_name=firstname, middlename=middlename, lastname=lastname,
                                    company=company))

        finally:
            cursor.close()
        return list

    def get_member_list_with_merged_emails_and_phones(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, fax, email, email2, email3) = row
                list.append(
                    Contact(id=str(id), first_name=firstname, lastname=lastname, address=address,
                            all_phones_from_home_page=home + mobile + work + fax,
                            all_emails_from_home_page=email + email2 + email3))
        finally:
            cursor.close()
        return list

    def get_member_list_as_at_ui(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, fax) = row
                list.append(
                    Contact(id=str(id), first_name=firstname, lastname=lastname, address=address, home=home,
                            mobile=mobile, work=work, fax=fax, email=email, email2=email2, email3=email3,
                            all_emails_from_db=email + email2 + email3, all_phones_from_db=home + mobile + work + fax))
        finally:
            cursor.close()
        return list
