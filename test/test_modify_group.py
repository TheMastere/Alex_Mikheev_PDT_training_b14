
from model.group import Group

def test_modify_group(app):
    app.group.modify_group(Group(name="gjjgekglelkr", header="iireeorererp", footer="ijgegegoegoegko"))

def test_modify_group_name(app):
    app.group.modify_group(Group(name="NewNewGroup1"))

def test_modify_group_header(app):
    app.group.modify_group(Group(header="NewHeader111"))
