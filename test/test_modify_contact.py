from model.contact import New_contact
from random import randrange


def test_modify_contact(app):
    if app.group_new_contact.count() == 0:
        app.group_new_contact.add_new_contact(
            New_contact(firstname="Alex", middlename="fffefe", lastname="wfawf", nickname="fwwfett", title="wfwfwer",
                        company="erreeg",
                        address="fwfawfaf fwfwaf fferwrr", homephone="454655665", mobilephone="89077777777", workphone="5656565656",
                        fax="809876",
                        email="fesefsf@mail.ru", email1="fwfwf@mail.ru", email2="wfwfwfwfrer@gg.ru", email3="fwghehjrlt@ruru", address2="awwaagwg ffeef fefert", secondary_phone="89066666666",
                        notes="awfawafwa fjfjhw fehgerrt"))
    old_contacts = app.group_new_contact.get_contact_list()
    index = randrange(len(old_contacts))
    contacts = New_contact(firstname="Niokolay", middlename="ggggg", lastname="Stekolnikov", nickname="Steklov",
                           title="razotr",
                           company="bichpacket",
                           address="kifwwf owowif pwofpwf", homephone="34454545", mobilephone="89766666777", workphone="45455445",
                           fax="97632",
                           email="fesefsf@mail.ru", email1="fwfwf@mail.ru", email2="wfwfwfwfrer@gg.ru", email3="fwghehjrlt@ruru", address2="gwiiree ierjjie oerperpe", secondary_phone="8973333333",
                           notes="jfkwkjfkw jwfjwfj whfhwfhwfwfiwffw")
    contacts.id = old_contacts[index].id
    app.group_new_contact.modify_contact_by_index(index, contacts)
    new_contacts = app.group_new_contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contacts
    assert sorted(old_contacts, key=New_contact.id_or_max) == sorted(new_contacts, key=New_contact.id_or_max)

# def test_modify_contact_firstname(app):
#     old_contacts = app.group_new_contact.get_contact_list()
#     if app.group_new_contact.count() == 1:
#         app.group_new_contact.modify_contact(
#             New_contact(firstname="Koleksandr111"))
#     new_contacts = app.group_new_contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_modify_contact_address(app):
#     old_contacts = app.group_new_contact.get_contact_list()
#     if app.group_new_contact.count() == 1:
#         app.group_new_contact.modify_contact(
#             New_contact(address="NOadress nowadhhge g111ert"))
#     new_contacts = app.group_new_contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
