# -*- coding: utf-8 -*-
from model.contact_information import ContactInfo

#def test_add_new_empty_contact(app):
    #app.open_home_page()
    #old_contacts = app.contact.get_contact_list()
    #contact = ContactInfo(address ="", company ="", firstname ="", home ="", lastname ="")
    #app.contact.fill_new_form(contact)
    #app.open_home_page()
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) +1 == len(new_contacts)
    #old_contacts.append(contact)
    #assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)

def test_add_new_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    contact_info = ContactInfo(address ="Минск, Беларусь", company ="ZippyBus", firstname ="Елена", home ="224616", lastname ="Прокорым")
    app.contact.fill_new_form(contact_info)
    app.open_home_page()

    assert app.contact.count() - len(old_contacts) == 1
    #assert len(new_contacts) - len(old_contacts) == 1
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact_info)
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)

