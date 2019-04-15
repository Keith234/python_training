import re
from random import randrange

from model.contact import Contact


def test_information_comparison_between_homepage_and_edit_page(app):
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_information_comparison_between_homepage_and_data_base(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Nana", middlename="Ver", lastname="Ko"))
    else:
        pass
    contacts_from_home_page = app.contact.get_contact_list()
    contact_from_data_base = db.get_member_list_as_at_ui()
    assert len(contacts_from_home_page) == len(contact_from_data_base)

    contacts_from_home_page_sorted = sorted(contacts_from_home_page, key=Contact.id_or_max)
    contact_from_data_base_sorted = sorted(contact_from_data_base, key=Contact.id_or_max)
    for x in range(len(contacts_from_home_page_sorted)):
        assert contacts_from_home_page_sorted[x].first_name == contact_from_data_base_sorted[x].first_name.strip()
        assert contacts_from_home_page_sorted[x].lastname == contact_from_data_base_sorted[x].lastname.strip()
        assert contacts_from_home_page_sorted[x].address == contact_from_data_base_sorted[x].address
        assert contacts_from_home_page_sorted[x].all_emails_from_home_page == merge_emails_like_on_home_page(
            contact_from_data_base_sorted[x])
        assert contacts_from_home_page_sorted[x].all_phones_from_home_page == merge_phones_like_on_home_page(
            contact_from_data_base_sorted[x])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.home, contact.mobile,
                                                                               contact.work,
                                                                               contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.email, contact.email2,
                                                                               contact.email3]))))
