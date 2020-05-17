from model.group_new_contact import New_contact


def test_delete_contact(app):
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
        old_contacts = app.group_new_contact.get_contact_list()
        app.group_new_contact.delete_contact()
        new_contacts = app.group_new_contact.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts[0:1] = []
        assert old_contacts == new_contacts
