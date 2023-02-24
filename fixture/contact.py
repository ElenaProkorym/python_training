class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_new_form(self, contact_info):
        wd = self.app.wd
        # Add new contact
        wd.find_element_by_link_text("add new").click()
        # Fill contact form
        # First name
        self.set_first_name(contact_info)
        # Last name
        self.set_last_name(contact_info)
        # fill company
        self.set_company(contact_info)
        # fill address
        self.set_address(contact_info)
        # fill telephone
        self.set_home(contact_info)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def set_home(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact_info.home)

    def set_address(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact_info.address)

    def set_company(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact_info.company)

    def click_delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def click_edit_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def click_update_button(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def set_email(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact_info.email)

    def set_first_name(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact_info.firstname)

    def set_last_name(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact_info.lastname)
