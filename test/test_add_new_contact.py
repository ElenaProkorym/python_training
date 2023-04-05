# -*- coding: utf-8 -*-
from model.contact_information import ContactInfo

def test_add_new_contact(app,db, json_contacts):
    contact_info = json_contacts
    app.open_home_page()
    old_contacts = db.get_contact_list()
    app.contact.fill_new_form(contact_info)
    app.open_home_page()

    new_contacts = db.get_contact_list()
    old_contacts.append(contact_info)
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)
