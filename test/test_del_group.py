from model.group import Group
def test_delete_first_group(app):
    if app.group.count() == 0:
        group = Group(name = "test")
        app.group.create(group)
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - len(new_groups)== 1
    old_groups[0:1] = []
    assert old_groups == new_groups




