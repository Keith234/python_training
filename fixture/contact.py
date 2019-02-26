import time


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def chenge_contact_field_value(self, field_name, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.chenge_contact_field_value("firstname", contact.first_name)
        self.chenge_contact_field_value("middlename", contact.middlename)
        self.chenge_contact_field_value("lastname", contact.lastname)
        self.chenge_contact_field_value("nickname", contact.nicknam)
        self.chenge_contact_field_value("title", contact.title)
        self.chenge_contact_field_value("company", contact.company)
        self.chenge_contact_field_value("address", contact.address)
        self.chenge_contact_field_value("home", contact.home)
        self.chenge_contact_field_value("mobile", contact.mobile)
        self.chenge_contact_field_value("work", contact.work)
        self.chenge_contact_field_value("fax", contact.fax)
        self.chenge_contact_field_value("email", contact.email)
        self.chenge_contact_field_value("email2", contact.email2)
        self.chenge_contact_field_value("email3", contact.email3)

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('td [type="checkbox"]').click()
        wd.find_element_by_css_selector('div [value="Delete"]').click()
        wd.switch_to_alert().accept()
        time.sleep(5)

    def modify_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_css_selector('img[title="Edit"]').click()
        self.fill_contact_form(contact)
        wd.find_element_by_name('update').click()
