import time

from model.contact import Contact
import re


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

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # find a row
        row = wd.find_elements_by_name("entry")[index]
        # find a cell
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_to_edit_by_index(index)
        wd.find_element_by_css_selector('div [value="Delete"]').click()
        time.sleep(5)
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        wd.find_element_by_name('update').click()
        self.contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # find a row
        row = wd.find_elements_by_name("entry")[index]
        # find a cell
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

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
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(
                    Contact(id=id, lastname=lastname, first_name=first_name, address=address,
                            all_phones_from_home_page=all_phones,
                            all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(lastname=lastname, first_name=firstname, address=address, id=id, home=home, mobile=mobile,
                       work=work, secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, secondaryphone=secondaryphone)
