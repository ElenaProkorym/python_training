from model.group import Group
from random import randrange
import random
def test_edit_group_name(app,db,check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name ="Test group")
    group.id = old_groups [index].id

    app.group.edit_group_by_id(group.id, group)

    new_groups = db.get_group_list()
    old_groups [index]=group
    if check_ui:
        assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


