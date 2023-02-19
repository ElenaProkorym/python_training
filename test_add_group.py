# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest

@pytest.fixture
def helper(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(helper):
    helper.login(username ="admin", password ="secret")
    helper.create_group(Group(name ="group1", header ="Feb", footer ="New group created"))
    helper.logout()

def test_add_empty_group(helper):
    helper.login(username ="admin", password ="secret")
    helper.create_group(Group(name ="", header ="", footer =""))
    helper.logout()
