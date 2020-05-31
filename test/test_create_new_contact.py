# -*- coding: utf-8 -*-
from model.contact import New_contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [New_contact(firstname=firstname, middlename=middlename, lastname=lastname, address=address,
                        homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                        email=email, secondary_phone=secondary_phone)
            for firstname in ["", random_string("firstname", 10)]
            for middlename in ["", random_string("middlename", 10)]
            for lastname in ["", random_string("lastname", 10)]
            for address in ["", random_string("address", 20)]
            for homephone in ["", random_string("homephone", 7)]
            for mobilephone in ["", random_string("mobilephone", 7)]
            for workphone in ["", random_string("workphone", 7)]
            for email in ["", random_string("email", 10)]
            for secondary_phone in ["", random_string("secondary_phone", 7)]]

@pytest.mark.parametrize("new_contact", testdata, ids=[repr(x) for x in testdata])
def test_create_new_contact(app, new_contact):
    old_contacts = app.group_new_contact.get_contact_list()
    app.group_new_contact.add_new_contact(new_contact)
    assert len(old_contacts) + 1 == app.group_new_contact.count()
    new_contacts = app.group_new_contact.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=New_contact.id_or_max) == sorted(new_contacts, key=New_contact.id_or_max)
