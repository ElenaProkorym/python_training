from model.contact_information import ContactInfo
import time
def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_new_form(ContactInfo())
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.select_first_contact()
    app.contact.click_delete_first_contact()
    app.wd.switch_to.alert.accept()
    # Give the browser time to delete contact
    time.sleep(3)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) -1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts