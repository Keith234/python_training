# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", middlename="", lastname="", nicknam="",
                    title="", company="", address="", home="",
                    mobile="", work="", fax="", secondaryphone="",
                    email="", email2="",
                    email3="")] + \
           [Contact(first_name=random_string("first_name", 8), middlename=random_string("middlename", 10),
                    lastname=random_string("lastname", 11), nicknam=random_string("nicknam", 5),
                    title=random_string("title", 4), company=random_string("company", 12),
                    address=random_string("address", 25), home=random_string("home", 7),
                    mobile="045364636363", work="64646464", fax="85463543", secondaryphone="5364",
                    email=random_string("email", 10), email2=random_string("email2", 10),
                    email3=random_string("email3", 10))
            for i in range(5)
            ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
