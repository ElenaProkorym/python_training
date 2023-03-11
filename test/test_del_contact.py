from model.contact_information import ContactInfo
from random import  randrange
import time

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_new_form(ContactInfo())
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.select_contact_by_index(index)

    app.contact.click_delete_contact()
    app.wd.switch_to.alert.accept()
    # Give the browser time to delete contact
    time.sleep(3)

    assert len(old_contacts) - app.contact.count()==1
    #assert len(old_contacts) - len(new_contacts) == 1
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts