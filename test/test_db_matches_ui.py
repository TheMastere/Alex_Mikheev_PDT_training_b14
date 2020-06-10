from model.group import Group
from model.contact import New_contact


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_contact_list(app, db):
    ui_list = app.group_new_contact.get_contact_list()
    def clean(group_new_contact):
        return New_contact(id=group_new_contact.id, firstname=group_new_contact.firstname.strip(), lastname=group_new_contact.lastname.strip())
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=New_contact.id_or_max) == sorted(db_list, key=New_contact.id_or_max)