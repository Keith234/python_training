from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Nana", middlename="Ver", lastname="Ko"))
    app.contact.delete_first_contact()
