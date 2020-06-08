from model.group import Group
import random


def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testtesttest"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups = group
    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_name(app):
    #  old_groups = app.group.get_group_list()
    # if app.group.count() == 1:
    #     app.group.modify_group(Group(name="NewNewGroup1"))
    # new_groups = app.group.get_group_list()
    # assert len(old_groups) == len(new_groups)


# def test_modify_group_header(app):
    #  old_groups = app.group.get_group_list()
    #  if app.group.count() == 1:
    #     app.group.modify_group(Group(header="NewHeader111"))
    # new_groups = app.group.get_group_list()
    # assert len(old_groups) == len(new_groups)
