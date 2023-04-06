from model.group import Group
from random import randrange
import random
def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test"))
    old_groups = get_groups(check_ui, app, db)
    group= random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = get_groups(check_ui, app, db)
    assert len(old_groups) - len(new_groups)== 1
    assert sorted(new_groups, key= Group.id_or_max) == sorted(app.group.get_group_list(), key= Group.id_or_max)
    old_groups.remove(group)

def get_groups(check_ui, app, db):
    if check_ui:
        return app.group.get_group_list()
    else:
        return db.get_group_list()





