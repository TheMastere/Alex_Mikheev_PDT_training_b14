# -*- coding: utf-8 -*-
from model.contact import New_contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " *10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [New_contact(firstname="", middlename="", lastname="", address="",
                        homephone="", mobilephone="", workphone="",
                        email="", secondary_phone="")] + [
               New_contact(firstname=random_string("name", 10), middlename=random_string("name", 10),
                           lastname=random_string("name", 10), address=random_string("name", 20),
                           homephone=random_string("name", 7), mobilephone=random_string("name", 7),
                           workphone=random_string("name", 7),
                           email=random_string("name", 10), secondary_phone=random_string("name", 7))
]

@pytest.mark.parametrize("new_contact", testdata, ids=[repr(x) for x in testdata])
def test_create_new_contact(app, new_contact):
    old_contacts = app.group_new_contact.get_contact_list()
    app.group_new_contact.add_new_contact(new_contact)
    assert len(old_contacts) + 1 == app.group_new_contact.count()
    new_contacts = app.group_new_contact.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=New_contact.id_or_max) == sorted(new_contacts, key=New_contact.id_or_max)
