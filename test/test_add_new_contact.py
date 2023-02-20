# -*- coding: utf-8 -*-
from model.contact_information import Contactinfo
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_empty_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.fill_new_form(Contactinfo(address ="", company ="", firstname ="", home ="", lastname =""))
    app.session.logout()

def test_add_new_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.fill_new_form(Contactinfo(address ="Минск, Беларусь", company ="ZippyBus", firstname ="Елена", home ="224616", lastname ="Прокорым"))
    app.session.logout()

