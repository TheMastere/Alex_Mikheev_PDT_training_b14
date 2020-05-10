from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(Group(name="gjjgekglelkr", header="iireeorererp", footer="ijgegegoegoegko"))
    app.session.logout()

def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(Group(name="NewNewGroup1"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(Group(header="NewHeader111"))
    app.session.logout()