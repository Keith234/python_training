from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="Dina", middlename="Tor", lastname="Mia", nicknam="Mom",
                                             title="TJT", company="JIT", address="45 Street", home="0985477",
                                             mobile="0453665363", work="6468964", fax="86543",
                                             email="856tgh@gmail.com", email2="ujjjbhg@gmail.com",
                                             email3="jhyt6g@gmail.com", bday="20", bmonth="November", byear="1993",
                                             aday="17",
                                             amonth="July", ayear="2018", address2="uytUYTgfghj", phone2="64546",
                                             notes="sfdtyufjfjjfv etfd"))

    app.session.logout()
