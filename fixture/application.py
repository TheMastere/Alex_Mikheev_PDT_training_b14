from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.group_new_contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(7)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.group_new_contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
