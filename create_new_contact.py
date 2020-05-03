# -*- coding: utf-8 -*-
import pytest
from new_contact import New_contact
from application_new_contact import Application_new_contact


@pytest.fixture
def app(request):
    fixture = Application_new_contact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_new_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact()
    app.fill_new_form_for_add_new_contact(
        New_contact(firstname="Alex", middlename="fffefe", lastname="wfawf", nickname="fwwfett", title="wfwfwer",
                    company="erreeg",
                    address="fwfawfaf fwfwaf fferwrr", home="wfwff", mobile="89077777777", work="wrefddf", fax="809876",
                    email="fesefsf@mail.ru", address2="awwaagwg ffeef fefert", phone2="89066666666",
                    notes="awfawafwa fjfjhw fehgerrt"))
    app.submit_new_contact()
    app.logout()
