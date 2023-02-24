
def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.open_home_page()
    app.contact.select_first_contact()
    app.contact.click_delete_first_contact()
    app.wd.switch_to.alert.accept()
    app.session.logout()