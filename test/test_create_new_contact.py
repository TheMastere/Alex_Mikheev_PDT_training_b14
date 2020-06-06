# -*- coding: utf-8 -*-
from model.contact import New_contact


def test_create_new_contact(app, json_contacts):
    new_contact = json_contacts
    old_contacts = app.group_new_contact.get_contact_list()
    app.group_new_contact.add_new_contact(new_contact)
    assert len(old_contacts) + 1 == app.group_new_contact.count()
    new_contacts = app.group_new_contact.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=New_contact.id_or_max) == sorted(new_contacts, key=New_contact.id_or_max)
