from model.contact_information import ContactInfo
def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_new_form(ContactInfo())

    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.click_edit_first_contact()
    contact_info = ContactInfo(lastname="Лисица", email="ivanov@rambler.ru")
    app.contact.set_last_name(contact_info)
    app.contact.set_email(contact_info)
    app.contact.click_update_button()
    app.open_home_page()

    contact_info.id = old_contacts[0].id

    assert len(old_contacts) == app.contact.count()
    #assert  len(old_contacts) == len(new_contacts)
    new_contacts = app.contact.get_contact_list()
    old_contacts[0]=contact_info
    assert sorted(old_contacts, key=ContactInfo.id_or_max) == sorted(new_contacts, key=ContactInfo.id_or_max)

    #assert old_contacts[0] != new_contacts[0]

