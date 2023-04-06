from model.group import Group
from random import randrange
import random
def test_edit_group_name(app,db,check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = get_groups(check_ui, app, db)
    index = randrange(len(old_groups))
    group = Group(name ="Test group")
    group.id = old_groups [index].id

    app.group.edit_group_by_id(group.id, group)

    new_groups = get_groups(check_ui, app, db)
    old_groups [index]=group
    assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def get_groups(check_ui, app, db):
    if check_ui:
        return app.group.get_group_list()
    else:
        return db.get_group_list()