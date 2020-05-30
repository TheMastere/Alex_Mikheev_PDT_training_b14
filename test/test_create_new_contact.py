# -*- coding: utf-8 -*-
from model.contact import New_contact

def test_create_new_contact(app):
    old_contacts = app.group_new_contact.get_contact_list()
    contacts = New_contact(firstname="Alex", middlename="fffefe", lastname="wfawf", nickname="fwwfett", title="wfwfwer",
                        company="erreeg",
                        address="fwfawfaf fwfwaf fferwrr", home="454655665", mobile="89077777777", work="5656565656",
                        fax="809876",
                        email="fesefsf@mail.ru", address2="awwaagwg ffeef fefert", phone2="89066666666",
                        notes="awfawafwa fjfjhw fehgerrt")
    app.group_new_contact.add_new_contact(contacts)
    assert len(old_contacts) + 1 == app.group_new_contact.count()
    new_contacts = app.group_new_contact.get_contact_list()
    old_contacts.append(contacts)
    assert sorted(old_contacts, key=New_contact.id_or_max) == sorted(new_contacts, key=New_contact.id_or_max)