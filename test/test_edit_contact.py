from model.contact_information import ContactInfo
def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.open_home_page()
    app.contact.click_edit_first_contact()
    contact_info = ContactInfo(lastname="Иванов", email="ivanov@rambler.ru")
    app.contact.set_last_name(contact_info)
    app.contact.set_email(contact_info)
    app.contact.click_update_button()
    app.session.logout()