# -*- coding: utf-8 -*-
from model.contact_information import ContactInfo

def test_add_new_empty_contact(app):
    app.contact.fill_new_form(ContactInfo(address ="", company ="", firstname ="", home ="", lastname =""))

def test_add_new_contact(app):
    app.contact.fill_new_form(ContactInfo(address ="Минск, Беларусь", company ="ZippyBus", firstname ="Елена", home ="224616", lastname ="Прокорым"))

