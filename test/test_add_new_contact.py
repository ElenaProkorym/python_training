# -*- coding: utf-8 -*-
from model.contact_information import ContactInfo
import pytest
import random
import string
import re

def random_string(prefix, maxlen):
    symbols= string.ascii_letters + string.digits + " "
    name = prefix + " ".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + " "*10
    name = name.replace("'", "")  # remove single quotes
    return re.sub(" {2,}", " ", name).strip()  ## replace multiple whitespaces with one and trim whitespaces


contactdate =[ContactInfo(firstname ="", lastname = "", address = "", homephone = "",
    mobilephone = "", workphone = "", secondaryphone = "", company = "",
    email = "", email2 = "", email3 = "")] + [
    ContactInfo(firstname =random_string("firstname",10), lastname = random_string("lastname",10), address = random_string("address",20), homephone = random_string("homephone",10),
    mobilephone = random_string("mobilephone",10), workphone =random_string("workphone",10), secondaryphone = random_string("secondaryphone",10), company = random_string("company",20),
    email = random_string("email",20), email2 = random_string("email2",20), email3 = random_string("email3",20))
    for i in range (3)]

@pytest.mark.parametrize("contact_info", contactdate, ids=[repr(x) for x in contactdate])

def test_add_new_contact(app, contact_info):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.fill_new_form(contact_info)
    app.open_home_page()
    assert app.contact.count() - len(old_contacts) == 1
    #assert len(new_contacts) - len(old_contacts) == 1
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact_info)
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)
