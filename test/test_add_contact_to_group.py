from model.contact_information import ContactInfo
import random
from model.group import Group
from fixture.orm import ORMFixture

db= ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
def test_add_contact_to_group(app):
    app.open_home_page()
    if len(app.contact.get_contact_list()) == 0:
        app.contact.fill_new_form(ContactInfo())
        app.open_home_page()

    contacts_list = app.contact.get_contact_list()

    # Choose random contact
    contact = random.choice(contacts_list)
    app.contact.select_contact_by_id(contact.id)

    group_id = app.contact.click_add_to_group()

    group_contacts = db.get_contacts_in_group(Group(id=group_id))
    assert contact in group_contacts
