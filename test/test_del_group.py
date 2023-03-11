from model.group import Group
from random import randrange
def test_delete_some_group(app):
    if app.group.count() == 0:
        group = Group(name = "test")
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)

    assert len(old_groups) - app.group.count() == 1
    #assert len(old_groups) - len(new_groups)== 1
    new_groups = app.group.get_group_list()
    old_groups[index:index + 1] = []
    assert old_groups == new_groups





