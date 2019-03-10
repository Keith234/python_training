import time

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("theform")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

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
        self.delete_contact_by_index(0)

    def select_contact_by_index_and_click_edit(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector('img[title="Edit"]')[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index_and_click_edit(index)
        wd.find_element_by_css_selector('div [value="Delete"]').click()
        time.sleep(5)
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index_and_click_edit(index)
        self.fill_contact_form(contact)
        wd.find_element_by_name('update').click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector('img[title="Edit"]'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector('tr[name = "entry"]'):
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                first_name = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(lastname=lastname, first_name=first_name, id=id))
        return list(self.contact_cache)
