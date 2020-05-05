from model.group_modify import ModifyGroup


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(ModifyGroup(name="gjjgekglelkr", header="iireeorererp", footer="ijgegegoegoegko"))
    app.session.logout()
