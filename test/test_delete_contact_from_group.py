
from model.group import Group
from model.contact import New_contact
import random

def test_delete_contact_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="testtesttest"))
    if len(orm.get_contact_list()) == 0:
        app.group_new_contact.add_new_contact(
            New_contact(firstname="Alex", middlename="fffefe", lastname="wfawf", nickname="fwwfett", title="wfwfwer",
                        company="erreeg",
                        address="fwfawfaf fwfwaf fferwrr", homephone="454655665", mobilephone="89077777777",
                        workphone="5656565656",
                        fax="809876",
                        email="fesefsf@mail.ru", email1="fwfwf@mail.ru", email2="wfwfwfwfrer@gg.ru",
                        email3="fwghehjrlt@ruru", address2="awwaagwg ffeef fefert", secondary_phone="89066666666",
                        notes="awfawafwa fjfjhw fehgerrt"))
    all_groups = orm.get_group_list()
    group = random.choice(all_groups)
    all_contacts = orm.get_contact_list()
    contact = random.choice(all_contacts)
    if contact not in (orm.get_contacts_in_group(group)):
        app.group_new_contact.add_contact_to_group(contact, group)
    app.group_new_contact.delete_contact_from_group(contact, group)
    assert contact not in orm.get_contacts_in_group(group)