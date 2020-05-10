
from model.group_new_contact import New_contact

def test_modify_contact(app):
    app.group_new_contact.modify_contact(
        New_contact(firstname="Niokolay", middlename="ggggg", lastname="Stekolnikov", nickname="Steklov", title="razotr",
                    company="bichpacket",
                    address="kifwwf owowif pwofpwf", home="whitehime", mobile="89766666777", work="wiwiwff", fax="97632",
                    email="jfhwwfiwi@yandex.ru", address2="gwiiree ierjjie oerperpe", phone2="8973333333",
                    notes="jfkwkjfkw jwfjwfj whfhwfhwfwfiwffw"))

def test_modify_contact_firstname(app):
    app.group_new_contact.modify_contact(
        New_contact(firstname="Koleksandr111"))

def test_modify_contact_address(app):
    app.group_new_contact.modify_contact(
        New_contact(address="NOadress nowadhhge g111ert"))
