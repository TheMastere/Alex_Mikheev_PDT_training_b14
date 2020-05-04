from selenium import webdriver
from fixture.contact_session import SessionHelper
from fixture.group_new_contact import ContactHelper

class Application_new_contact:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.contact_session = SessionHelper(self)
        self.group_new_contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
