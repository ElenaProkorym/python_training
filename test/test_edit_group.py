from model.group import Group
def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name ="Name group")
    group.id = old_groups [0].id
    app.group.edit_first_group(group)

    assert len(old_groups) == app.group.count()
    #assert len(old_groups) == len(new_groups)
    new_groups = app.group.get_group_list()
    old_groups [0]=group
    assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_edit_group_header(app):
    #if app.group.count() == 0:
        #app.group.create(Group(name="test"))
    #app.group.edit_first_group(Group(header ="Name header"))


