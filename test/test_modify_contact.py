from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Nana", middlename="Ver", lastname="Ko"))
        app.contact.modify_first_contact(Contact(first_name="Dina", middlename="Tor", lastname="Mia", nicknam="Mom",
                                                 title="TJT", company="JIT", address="45 Street", home="0985477",
                                                 mobile="0453665363", work="6468964", fax="86543",
                                                 email="856tgh@gmail.com", email2="ujjjbhg@gmail.com",
                                                 email3="jhyt6g@gmail.com"))


def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Nana", middlename="Ver", lastname="Ko"))
    app.contact.modify_first_contact(Contact(first_name="Dana"))
