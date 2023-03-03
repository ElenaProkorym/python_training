from model.contact_information import ContactInfo
import time
def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_new_form(ContactInfo())
    app.open_home_page()
    app.contact.select_first_contact()
    app.contact.click_delete_first_contact()
    app.wd.switch_to.alert.accept()
    # Give the browser time to delete contact
    time.sleep(1)