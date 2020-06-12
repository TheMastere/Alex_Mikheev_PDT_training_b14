from random import randrange
from model.contact import New_contact


def test_matching_all_contacts_db(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.group_new_contact.add_new_contact(
            New_contact(firstname="Alex", middlename="fffefe", lastname="wfawf", nickname="fwwfett", title="wfwfwer",
                        company="erreeg",
                        address="fwfawfaf fwfwaf fferwrr", homephone="454655665", mobilephone="89077777777", workphone="5656565656",
                        fax="809876",
                        email="fesefsf@mail.ru", email1="fwfwf@mail.ru", email2="wfwfwfwfrer@gg.ru", email3="fwghehjrlt@ruru", address2="awwaagwg ffeef fefert", secondary_phone="89066666666",
                        notes="awfawafwa fjfjhw fehgerrt"))
    contacts_all = sorted(app.group_new_contact.get_contact_list(), key=New_contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=New_contact.id_or_max)
    c = 0
    for contact in contacts_all:
        contact_from_db = contacts_from_db[c]
        c = c+1
        assert contact.firstname == contact_from_db.firstname
        assert contact.lastname == contact_from_db.lastname
        assert contact.address == contact_from_db.address
        assert contact.all_phones_from_home_page == app.group_new_contact.merge_phones_like_on_home_page(contact_from_db)
        assert contact.all_email == app.group_new_contact.merge_emails_like_on_home_page(contact_from_db)
