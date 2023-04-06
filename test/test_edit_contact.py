import random
from model.contact_information import ContactInfo
from random import randrange
def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.fill_new_form(ContactInfo())

    app.open_home_page()
    old_contacts = get_contacts(check_ui, app, db)

    contact = random.choice(old_contacts)
    app.contact.click_edit_contact_by_id(contact.id)

    contact.lastname = "Малина"
    app.contact.set_last_name(contact)

    contact.email = "ivanov@rambler.ru"
    app.contact.set_email(contact)

    app.contact.click_update_button()
    app.open_home_page()

    new_contacts = get_contacts(check_ui, app, db)

    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)

def get_contacts(check_ui, app, db):
    if check_ui:
        return app.contact.get_contact_list()
    else:
        return db.get_contact_list()
