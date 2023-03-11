from model.contact_information import ContactInfo
class ContactHelper:

    def __init__(self, app):
        self.app = app

    contacts_cache = None

    def get_contact_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.contacts_cache = []
            for tr_element in wd.find_elements_by_css_selector("tr[name='entry']"):
                id = tr_element.find_element_by_name("selected[]").get_attribute("value")
                last_name = tr_element.find_element_by_css_selector("td:nth-child(2)").text
                first_name = tr_element.find_element_by_css_selector("td:nth-child(3)").text
                self.contacts_cache.append(ContactInfo(id = id, firstname=first_name, lastname= last_name))
        return list(self.contacts_cache)

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
        self.contacts_cache = None

    def count(self):
        wd = self.app.wd
        #self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def set_home(self, contact_info):
        if contact_info.home is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact_info.home)

    def set_address(self, contact_info):
        if contact_info.address is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact_info.address)

    def set_company(self, contact_info):
        if contact_info.company is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact_info.company)

    #def click_delete_first_contact(self):
        #self.click_delete_contact()

    def click_delete_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contacts_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def click_edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.contacts_cache = None

    def click_edit_first_contact(self):
        self.click_edit_contact_by_index(0)

    def click_update_button(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def set_email(self, contact_info):
        wd = self.app.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact_info.email)

    def set_first_name(self, contact_info):
        if contact_info.firstname is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact_info.firstname)

    def set_last_name(self, contact_info):
        if contact_info.lastname is None:
            return

        wd = self.app.wd
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact_info.lastname)
