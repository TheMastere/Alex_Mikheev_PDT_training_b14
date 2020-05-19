from model.group_new_contact import New_contact


def test_modify_contact(app):
    old_contacts = app.group_new_contact.get_contact_list()
    contacts = New_contact(firstname="Niokolay", middlename="ggggg", lastname="Stekolnikov", nickname="Steklov",
                           title="razotr",
                           company="bichpacket",
                           address="kifwwf owowif pwofpwf", home="whitehime", mobile="89766666777", work="wiwiwff",
                           fax="97632",
                           email="jfhwwfiwi@yandex.ru", address2="gwiiree ierjjie oerperpe", phone2="8973333333",
                           notes="jfkwkjfkw jwfjwfj whfhwfhwfwfiwffw")
    contacts.id = old_contacts[0].id
    app.group_new_contact.modify_contact(contacts)
    new_contacts = app.group_new_contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contacts
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
