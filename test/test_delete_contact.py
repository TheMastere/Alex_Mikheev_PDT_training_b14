


def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.group_new_contact.delete_contact()
    app.session.logout()