import random

from model.contact import Contact


def test_delete_contact_by_id(app, db):
    app.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Nana", middlename="Ver", lastname="Ko"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
