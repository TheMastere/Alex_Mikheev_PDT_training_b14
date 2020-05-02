# -*- coding: utf-8 -*-
import unittest
from new_contact import New_contact
from application_new_contact import Application_new_contact

class CreateNewContact(unittest.TestCase):
    def setUp(self):
        self.app = Application_new_contact()

    def test_create_new_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.add_new_contact()
        self.app.fill_new_form_for_add_new_contact(New_contact(firstname="Alex", middlename="fffefe", lastname="wfawf", nickname="fwwfett", title="wfwfwer", company="erreeg",
                                               address="fwfawfaf fwfwaf fferwrr", home="wfwff", mobile="89077777777", work="wrefddf", fax="809876",
                                               email="fesefsf@mail.ru", address2="awwaagwg ffeef fefert", phone2="89066666666",
                                               notes="awfawafwa fjfjhw fehgerrt"))
        self.app.submit_new_contact()
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
