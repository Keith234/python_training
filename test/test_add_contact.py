# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.open_contact_page()
    app.contact.create(Contact(first_name="Kevin", middlename="Ro", lastname="Tera", nicknam="Shadow",
                               title="TTT", company="New", address="Street", home="098787677",
                               mobile="045364636363", work="64646464", fax="85463543",
                               email="75hggh@gmail.com", email2="dfghjjbhg@gmail.com",
                               email3="jhfgcvg@gmail.com"))
