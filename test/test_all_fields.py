from model.contact import New_contact
from random import randrange


def test_all_fields_contact(app):
    if app.group_new_contact.count() == 0:
        app.group_new_contact.add_new_contact(
            New_contact(firstname="Alex", middlename="fffefe", lastname="wfawf", nickname="fwwfett", title="wfwfwer",
                        company="erreeg",
                        address="fwfawfaf fwfwaf fferwrr", homephone="454655665", mobilephone="89077777777", workphone="5656565656",
                        fax="809876",
                        email="fesefsf@mail.ru", email1="fwfwf@mail.ru", email2="wfwfwfwfrer@gg.ru", email3="fwghehjrlt@ruru", address2="awwaagwg ffeef fefert", secondary_phone="89066666666",
                        notes="awfawafwa fjfjhw fehgerrt"))
        all_contacts = app.contact.get_contact_list()
        index = randrange(len(all_contacts))
        contact = all_contacts[index]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
        assert contact.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
        assert contact.all_email == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
        assert contact.firstname == contact_from_edit_page.firstname
        assert contact.lastname == contact_from_edit_page.lastname
        assert contact.address == contact_from_edit_page.address