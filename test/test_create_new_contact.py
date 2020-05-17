# -*- coding: utf-8 -*-
from model.group_new_contact import New_contact

def test_create_new_contact(app):
    old_contacts = app.group_new_contact.get_contact_list()
    contacts = New_contact(firstname="Alex", middlename="fffefe", lastname="wfawf", nickname="fwwfett", title="wfwfwer",
                        company="erreeg",
                        address="fwfawfaf fwfwaf fferwrr", home="wfwff", mobile="89077777777", work="wrefddf",
                        fax="809876",
                        email="fesefsf@mail.ru", address2="awwaagwg ffeef fefert", phone2="89066666666",
                        notes="awfawafwa fjfjhw fehgerrt")
    app.group_new_contact.add_new_contact(contacts)
    new_contacts = app.group_new_contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=New_contact.id_or_max) == sorted(new_contacts, key=New_contact.id_or_max)
