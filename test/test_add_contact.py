# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Kevin", middlename="Ro", lastname="Tera", nicknam="Shadow",
                          title="TTT", company="New", address="Street", home="098787677",
                          mobile="045364636363", work="64646464", fax="85463543",
                          email="75hggh@gmail.com", email2="dfghjjbhg@gmail.com",
                          email3="jhfgcvg@gmail.com")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
