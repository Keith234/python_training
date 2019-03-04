from model.contact import Contact


def test_modify_first_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Nana", middlename="Ver", lastname="Ko"))
    contact = Contact(first_name="Dina", middlename="Tor", lastname="Mia", nicknam="Mom",
                      title="TJT", company="JIT", address="45 Street", home="0985477",
                      mobile="0453665363", work="6468964", fax="86543",
                      email="856tgh@gmail.com", email2="ujjjbhg@gmail.com",
                      email3="jhyt6g@gmail.com")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_name(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Nana", middlename="Ver", lastname="Ko"))
    contact = Contact(first_name="Dana")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
