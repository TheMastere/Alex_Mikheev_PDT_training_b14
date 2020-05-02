# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group
from application import Application

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application

    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="fffefegrre", header="ewwegrge", footer="wewefeg"))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
