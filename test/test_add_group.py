# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app, db,json_groups,check_ui):
    group = json_groups

    old_groups = get_groups(check_ui, app, db)
    app.group.create(group)

    new_groups = get_groups(check_ui, app, db)
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

def get_groups(check_ui, app, db):
    if check_ui:
        return app.group.get_group_list()
    else:
        return db.get_group_list()