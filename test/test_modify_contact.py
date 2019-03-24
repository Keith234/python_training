import random

from model.contact import Contact


def test_modify_contact_by_id(app, db, check_ui):
    app.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Nana", middlename="Ver", lastname="Ko"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    modified_contact = Contact(first_name="Dina", middlename="Tor", lastname="Mia", nicknam="Mom",
                               title="TJT", company="JIT", address="45 Street", home="0985477",
                               mobile="0453665363", work="6468964", fax="86543",
                               email="856tgh@gmail.com", email2="ujjjbhg@gmail.com",
                               email3="jhyt6g@gmail.com")
    modified_contact.id = contact.id
    app.contact.modify_contact_by_id(contact.id, modified_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(modified_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_first_contact_name(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Nana", middlename="Ver", lastname="Ko"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Dana")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
