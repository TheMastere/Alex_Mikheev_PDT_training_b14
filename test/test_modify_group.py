from model.group import Group


def test_modify_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="testtesttest"))
        app.group.modify_group(Group(name="gjjgekglelkr", header="iireeorererp", footer="ijgegegoegoegko"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 1:
        app.group.modify_group(Group(name="NewNewGroup1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 1:
        app.group.modify_group(Group(header="NewHeader111"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
