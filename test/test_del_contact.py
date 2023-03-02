from model.contact_information import ContactInfo
def test_delete_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.fill_new_form(ContactInfo(firstname ="test",address ="", company ="", home ="", lastname =""))
        app.open_home_page()
    app.contact.select_first_contact()
    app.contact.click_delete_first_contact()
    app.wd.switch_to.alert.accept()