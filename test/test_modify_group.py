from model.group import Group


def test_modify_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="testtesttest")
    group.id = old_groups[0].id
    app.group.modify_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


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
