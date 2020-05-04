# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="fffefegrre", header="ewwegrge", footer="wewefeg"))
    app.session.logout()