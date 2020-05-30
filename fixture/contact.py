from model.contact import New_contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/addressbook/" and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def add_new_contact(self, new_contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(new_contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_home_page()
        self.contact_cache = None

    def fill_new_form_for_add_new_contact(self, new_contact):
        wd = self.app.wd
        self.fill_contact_form(new_contact)

    def delete_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit delete contact
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_contact(self, new_contact):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # click button for edit contact
        wd.find_elements_by_xpath("(//img[@alt='Edit'])")[index].click()
        # fill contact form
        self.fill_contact_form(new_contact)
        # submit modification
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def fill_contact_form(self, new_contact):
        wd = self.app.wd
        self.change_field_contact("firstname", new_contact.firstname)
        self.change_field_contact("middlename", new_contact.middlename)
        self.change_field_contact("lastname", new_contact.lastname)
        self.change_field_contact("nickname", new_contact.nickname)
        self.change_field_contact("title", new_contact.title)
        self.change_field_contact("company", new_contact.company)
        self.change_field_contact("address", new_contact.address)
        self.change_field_contact("home", new_contact.homephone)
        self.change_field_contact("mobile", new_contact.mobilephone)
        self.change_field_contact("work", new_contact.workphone)
        self.change_field_contact("fax", new_contact.fax)
        self.change_field_contact("email", new_contact.email)
        self.change_field_contact("email", new_contact.email1)
        self.change_field_contact("email2", new_contact.email2)
        self.change_field_contact("email3", new_contact.email3)
        self.change_field_contact("address2", new_contact.address2)
        self.change_field_contact("phone2", new_contact.secondary_phone)
        self.change_field_contact("notes", new_contact.notes)

    def change_field_contact(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                id = row.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(
                    New_contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                all_phones_from_home_page=all_phones, all_email=all_email))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return New_contact(firstname=firstname, lastname=lastname, address=address, id=id, homephone=homephone, workphone=workphone,
                           mobilephone=mobilephone,
                           secondary_phone=secondary_phone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return New_contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                           secondary_phone=secondary_phone)
