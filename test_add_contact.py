# -*- coding: utf-8 -*-
import pytest
from application import Application
from contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(request.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="Kevin", middlename="Ro", lastname="Tera", nicknam="Shadow",
                               title="TTT", company="New", address="Street", home="098787677",
                               mobile="045364636363", work="64646464", fax="85463543",
                               email="75hggh@gmail.com", email2="dfghjjbhg@gmail.com",
                               email3="jhfgcvg@gmail.com", bday="11", bmonth="July", byear="1990", aday="15",
                               amonth="November", ayear="2011", address2="uytrdfghj", phone2="67",
                               notes="sfdtyedfetfd"))

    app.logout()
