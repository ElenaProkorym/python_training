# -*- coding: utf-8 -*-
from model.contact_information import ContactInfo
#from data.contacts import contactdate

#@pytest.mark.parametrize("contact_info", contactdate, ids=[repr(x) for x in contactdate])

def test_add_new_contact(app, json_contacts):
    contact_info = json_contacts
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.fill_new_form(contact_info)
    app.open_home_page()
    assert app.contact.count() - len(old_contacts) == 1
    #assert len(new_contacts) - len(old_contacts) == 1
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact_info)
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)
