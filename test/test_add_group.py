# -*- coding: utf-8 -*-
from model.group import Group
def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name ="group1", header ="Feb", footer ="New group created")
    app.group.create(group)

    assert app.group.count() - len(old_groups) == 1
    #assert len(old_groups) +1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

#def test_add_empty_group(app):
    #old_groups = app.group.get_group_list()
    #group = Group(name ="", header ="", footer ="")
    #app.group.create(group)
    #new_groups = app.group.get_group_list()
    #assert len(new_groups) - len(old_groups) == 1
    #old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)