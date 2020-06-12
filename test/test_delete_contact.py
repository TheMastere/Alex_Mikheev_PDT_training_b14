from model.contact import New_contact
from random import randrange


def test_delete_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.group_new_contact.add_new_contact(New_contact(firstname="Alex", middlename="fffefe", lastname="wfawf", nickname="fwwfett", title="wfwfwer",
                        company="erreeg",
                        address="fwfawfaf fwfwaf fferwrr", homephone="454655665", mobilephone="89077777777", workphone="5656565656",
                        fax="809876",
                        email="fesefsf@mail.ru", email1="fwfwf@mail.ru", email2="wfwfwfwfrer@gg.ru", email3="fwghehjrlt@ruru", address2="awwaagwg ffeef fefert", secondary_phone="89066666666",
                        notes="awfawafwa fjfjhw fehgerrt"))
        old_contacts = db.get_contact_list()
        index = randrange(len(old_contacts))
        app.group_new_contact.delete_contact_by_index(index)
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts[index:index+1] = []
        assert old_contacts == new_contacts
