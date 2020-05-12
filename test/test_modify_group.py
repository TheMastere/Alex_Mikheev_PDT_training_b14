
from model.group import Group

def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="testtesttest"))
        app.group.modify_group(Group(name="gjjgekglelkr", header="iireeorererp", footer="ijgegegoegoegko"))

def test_modify_group_name(app):
    if app.group.count() == 1:
        app.group.modify_group(Group(name="NewNewGroup1"))

def test_modify_group_header(app):
    if app.group.count() == 1:
        app.group.modify_group(Group(header="NewHeader111"))
