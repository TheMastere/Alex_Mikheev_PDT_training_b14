from model.group_new_contact import New_contact


def test_modify_contact(app):
    old_contacts = app.group_new_contact.get_contact_list()
    if app.group_new_contact.count() == 0:
        app.group_new_contact.add_new_contact()
        app.group_new_contact.fill_new_form_for_add_new_contact(
            New_contact(firstname="Alex", middlename="fffefe", lastname="wfawf", nickname="fwwfett", title="wfwfwer",
                        company="erreeg",
                        address="fwfawfaf fwfwaf fferwrr", home="wfwff", mobile="89077777777", work="wrefddf",
                        fax="809876",
                        email="fesefsf@mail.ru", address2="awwaagwg ffeef fefert", phone2="89066666666",
                        notes="awfawafwa fjfjhw fehgerrt"))
        app.group_new_contact.submit_new_contact()
        app.group_new_contact.modify_contact(
            New_contact(firstname="Niokolay", middlename="ggggg", lastname="Stekolnikov", nickname="Steklov",
                        title="razotr",
                        company="bichpacket",
                        address="kifwwf owowif pwofpwf", home="whitehime", mobile="89766666777", work="wiwiwff",
                        fax="97632",
                        email="jfhwwfiwi@yandex.ru", address2="gwiiree ierjjie oerperpe", phone2="8973333333",
                        notes="jfkwkjfkw jwfjwfj whfhwfhwfwfiwffw"))
    new_contacts = app.group_new_contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_firstname(app):
    old_contacts = app.group_new_contact.get_contact_list()
    if app.group_new_contact.count() == 1:
        app.group_new_contact.modify_contact(
            New_contact(firstname="Koleksandr111"))
    new_contacts = app.group_new_contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_address(app):
    old_contacts = app.group_new_contact.get_contact_list()
    if app.group_new_contact.count() == 1:
        app.group_new_contact.modify_contact(
            New_contact(address="NOadress nowadhhge g111ert"))
    new_contacts = app.group_new_contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
