# -*- coding: utf-8 -*-
from contact_information import Contactinfo
from contact_app import ContactApplication
import pytest

@pytest.fixture
def capp(request):
    fixture = ContactApplication()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_empty_contact(capp):
    capp.login(username = "admin", password = "secret")
    capp.fill_new_contact_form(Contactinfo(address = "", company = "", firstname = "", home = "", lastname = ""))
    capp.logout()

def test_add_new_contact(capp):
    capp.login(username = "admin", password = "secret")
    capp.fill_new_contact_form(Contactinfo(address = "Минск, Беларусь", company = "ZippyBus", firstname = "Елена", home ="224616", lastname = "Прокорым"))
    capp.logout()

