from model.contact_information import ContactInfo
from random import  randrange
import time
import  random
def test_delete_some_contact(app,db,check_ui):
    app.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.fill_new_form(ContactInfo())
    app.open_home_page()

    old_contacts = get_contacts(check_ui, app, db)

    contact= random.choice(old_contacts)
    app.contact.select_contact_by_id(contact.id)

    app.contact.click_delete_contact()
    app.wd.switch_to.alert.accept()
    # Give the browser time to delete contact
    time.sleep(3)

    assert len(old_contacts) - app.contact.count()==1

    new_contacts = get_contacts(check_ui, app, db)

    assert sorted(new_contacts, key=ContactInfo.id_or_max) == sorted(app.contact.get_contact_list(),key=ContactInfo.id_or_max)
    old_contacts.remove(contact)

def get_contacts(check_ui, app, db):
    if check_ui:
        return app.contact.get_contact_list()
    else:
        return db.get_contact_list()